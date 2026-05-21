import allure
import pytest
from services.auth.auth_service import AuthService
from services.auth.models.login_request import LoginRequest
from services.auth.models.login_response import LoginResponse
from core.config import config


@allure.feature("API: Аутентификация")
class TestAuthApi:

    @allure.title("POST /auth/login — успешный логин")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_login_success(self, auth_service):
        with allure.step("Отправить запрос на логин с валидными кредами"):
            response = auth_service.login(LoginRequest(
                email=config.test_user_email,
                password=config.test_user_password
            ))

        with allure.step("Проверить структуру ответа через Pydantic"):
            assert isinstance(response, LoginResponse)

        with allure.step("Проверить что токен не пустой"):
            assert response.token, "Токен пустой"

        with allure.step("Проверить данные пользователя"):
            assert response.user.email == config.test_user_email
            assert response.user.emailVerified is True

    @allure.title("POST /auth/login — неверный пароль возвращает 401")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_login_wrong_password(self, api_utils_anon):
        with allure.step("Отправить запрос с неверным паролем"):
            response = api_utils_anon.post(
                "/auth/login",
                json={
                    "email": config.test_user_email,
                    "password": "wrong_password_123"
                }
            )

        with allure.step("Проверить статус код 401"):
            assert response.status_code == 401, \
                f"Ожидали 401, получили {response.status_code}"

    @allure.title("GET /auth/me — получить данные текущего пользователя")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_get_me(self, auth_service, api_utils_auth):
        with allure.step("Получить данные текущего пользователя"):
            auth_service_auth = AuthService(api_utils_auth)
            me = auth_service_auth.get_me()

        with allure.step("Проверить структуру ответа через Pydantic"):
            from services.auth.models.me_response import MeResponse
            assert isinstance(me, MeResponse)

        with allure.step("Проверить email"):
            assert me.email == config.test_user_email