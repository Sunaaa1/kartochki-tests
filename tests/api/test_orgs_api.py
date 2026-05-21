import allure
import pytest
from services.orgs.models.org_response import OrgResponse


@allure.feature("API: Организация")
class TestOrgsApi:

    @allure.title("GET /orgs/me — получить данные организации")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_get_org_me(self, orgs_service):
        with allure.step("Получить данные организации"):
            response = orgs_service.get_me()

        with allure.step("Проверить структуру ответа через Pydantic"):
            assert isinstance(response, OrgResponse)

        with allure.step("Проверить что план организации валидный"):
            assert response.plan in ["free", "pro", "enterprise"], \
                f"Неожиданный план: {response.plan}"

        with allure.step("Проверить что кредиты неотрицательные"):
            assert response.creditsRemaining >= 0
            assert response.creditsPurchased >= 0
            assert response.creditsUsed >= 0