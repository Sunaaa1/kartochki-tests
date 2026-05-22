import allure
import pytest
from services.orgs.models.plan_response import PlanResponse
from services.orgs.models.purchase_response import PurchaseResponse


@allure.feature("API: Биллинг")
class TestBillingApi:

    @allure.title("GET /orgs/plans — получить список тарифных планов")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_get_plans(self, orgs_service_auth):
        with allure.step("Получить список планов"):
            plans = orgs_service_auth.get_plans()

        with allure.step("Проверить структуру ответа"):
            assert len(plans) > 0
            for plan in plans:
                assert isinstance(plan, PlanResponse)

        with allure.step("Проверить что план free существует"):
            free_plan = next((p for p in plans if p.id == "free"), None)
            assert free_plan is not None, "План free не найден"
            assert free_plan.priceRub == 0, "Free план должен быть бесплатным"

        with allure.step("Проверить что pro дороже free"):
            pro_plan = next((p for p in plans if p.id == "pro"), None)
            assert pro_plan is not None
            assert pro_plan.priceRub > free_plan.priceRub

        with allure.step("Проверить что enterprise дороже pro"):
            enterprise_plan = next((p for p in plans if p.id == "enterprise"), None)
            assert enterprise_plan is not None
            assert enterprise_plan.priceRub > pro_plan.priceRub

    @allure.title("POST /orgs/credits/purchase — недостаточно средств возвращает 400")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_purchase_credits_insufficient_funds(self, orgs_service_auth):
        with allure.step("Отправить запрос с суммой превышающей баланс"):
            response = orgs_service_auth.orgs_helper.post_purchase(
                json={"credits": 100, "amountRubKopecks": 149000}
            )

        with allure.step("Проверить что сервер вернул 400 — недостаточно средств"):
            assert response.status_code == 400
            assert "Недостаточно средств" in response.json()["message"]

    @allure.title("POST /orgs/credits/purchase — отрицательное количество кредитов возвращает 400")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_purchase_credits_negative(self, orgs_service_auth):
        with allure.step("Отправить запрос с отрицательным количеством кредитов"):
            response = orgs_service_auth.orgs_helper.post_purchase(
                json={"credits": -1, "amountRubKopecks": 149000}
            )

        with allure.step("Проверить статус код 400"):
            assert response.status_code == 400, \
                f"Ожидали 400, получили {response.status_code}"

    @allure.title("POST /orgs/credits/purchase — несоответствие суммы и кредитов")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_purchase_credits_wrong_amount(self, orgs_service_auth):
        with allure.step("Отправить запрос с неверной суммой для 100 кредитов"):
            response = orgs_service_auth.orgs_helper.post_purchase(
                json={"credits": 100, "amountRubKopecks": 1}
            )

        with allure.step("Проверить что сервер отклонил несоответствующую сумму"):
            assert response.status_code == 400, \
                f"Сервер принял неверную сумму, статус: {response.status_code}"
