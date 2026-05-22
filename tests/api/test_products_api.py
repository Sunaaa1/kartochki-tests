import allure
import pytest
from services.products.models.product_request import MarketplaceEnum
from services.products.models.product_response import ProductResponse, ProductStatusEnum
from services.products.models.products_list_response import ProductsListResponse

TEST_IMAGE_URL = "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=800"


@allure.feature("API: Товары")
class TestProductsApi:

    @allure.title("GET /products — получить список товаров")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_get_products(self, products_service):
        with allure.step("Получить список товаров"):
            response = products_service.get_products()

        with allure.step("Проверить структуру ответа"):
            assert isinstance(response, ProductsListResponse)

        with allure.step("Проверить поля пагинации"):
            assert response.page >= 1
            assert response.limit > 0
            assert response.total >= 0

    @allure.title("POST /products — создать товар с валидными данными")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_create_product_success(self, products_service):
        with allure.step("Создать товар по URL"):
            response = products_service.create_product(
                image_url=TEST_IMAGE_URL,
                marketplace=MarketplaceEnum.WILDBERRIES
            )

        with allure.step("Проверить структуру ответа"):
            assert isinstance(response, ProductResponse)

        with allure.step("Проверить что товар создан со статусом pending"):
            assert response.status == ProductStatusEnum.PENDING

        with allure.step("Проверить что данные совпадают с запросом"):
            assert response.imageUrl == TEST_IMAGE_URL
            assert response.marketplace == MarketplaceEnum.WILDBERRIES
            assert response.id is not None

    @allure.title("POST /products — создать товар с невалидным URL возвращает 400")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    @pytest.mark.xfail(
        strict=True,
        reason="BUG: сервер принимает пустой imageUrl вместо возврата 400."
    )
    def test_create_product_invalid_url(self, products_service):
        with allure.step("Отправить запрос с невалидными данными"):
            response = products_service.products_helper.post_product(
                json={"imageUrl": "", "marketplace": "wildberries"}
            )

        with allure.step("Проверить статус код 400"):
            assert response.status_code == 400