import allure
import pytest
from services.products.models.product_request import MarketplaceEnum
from core.config import config


@allure.feature("DB: Валидация данных")
class TestDbValidation:

    @allure.title("Пользователь существует в БД после регистрации")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.db
    def test_user_exists_in_db(self, db):
        with allure.step("Найти пользователя в БД по email"):
            row = db.fetch_one(
                "SELECT id, email, email_verified_at FROM users WHERE email = :email",
                {"email": config.test_user_email}
            )

        with allure.step("Проверить что пользователь существует"):
            assert row is not None, f"Пользователь {config.test_user_email} не найден в БД"

        with allure.step("Проверить что email подтверждён"):
            assert row.email_verified_at is not None, "Email не подтверждён"

    @allure.title("Создание товара — данные корректно сохраняются в БД")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.db
    def test_product_saved_in_db(self, products_service, db):
        product = None
        try:
            with allure.step("Создать товар через API"):
                product = products_service.create_product(
                    image_url="https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=800",
                    marketplace=MarketplaceEnum.WILDBERRIES
                )

            with allure.step("Проверить статус из API ответа — pending"):
                assert product.status == "pending", \
                    f"API вернул неожиданный статус: {product.status}"

            with allure.step("Найти товар в БД"):
                row = db.fetch_one(
                    "SELECT id, status, marketplace, image_url, org_id FROM products WHERE id = :id",
                    {"id": product.id}
                )

            with allure.step("Проверить что товар существует в БД"):
                assert row is not None, f"Товар {product.id} не найден в БД"

            with allure.step("Проверить что статус в БД валидный"):
                assert row.status in ["pending", "processing", "completed", "failed"], \
                    f"Неожиданный статус в БД: {row.status}"

            with allure.step("Проверить marketplace в БД"):
                assert row.marketplace == "wildberries"

            with allure.step("Проверить image_url в БД"):
                assert row.image_url == "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=800"

        finally:
            if product:
                with allure.step("Teardown — удалить тестовый товар из БД"):
                    db.execute_dml(
                        "DELETE FROM products WHERE id = :id",
                        {"id": product.id}
                    )

    @allure.title("Кредитные транзакции организации существуют в БД")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.db
    def test_credit_transactions_in_db(self, api_utils_auth, db):
        with allure.step("Получить orgId текущего пользователя"):
            from services.auth.auth_service import AuthService
            auth_service_auth = AuthService(api_utils_auth)
            me = auth_service_auth.get_me()
            org_id = me.orgId

        with allure.step("Получить транзакции из БД"):
            rows = db.execute(
                """
                SELECT id, amount, type, description 
                FROM credit_transactions 
                WHERE org_id = :org_id 
                ORDER BY created_at DESC 
                LIMIT 5
                """,
                {"org_id": org_id}
            )

        with allure.step("Проверить что транзакции существуют"):
            assert len(rows) > 0, "Транзакции не найдены в БД"

        with allure.step("Проверить структуру транзакций"):
            for tx in rows:
                assert tx.type in ["debit", "credit"]
                assert tx.amount != 0
                assert tx.description is not None