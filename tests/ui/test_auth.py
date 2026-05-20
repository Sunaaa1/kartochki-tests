import allure
import pytest
from faker import Faker
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from core.config import config
from core.logger import Logger

fake = Faker()

@allure.feature("Аутентификация")
class TestAuth:

    @allure.title("Успешный логин с валидными кредами")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_login_success(self, page):
        Logger.info("TEST: test_login_success started")

        with allure.step("Открыть страницу логина"):
            login_page = LoginPage(page)
            login_page.open()
            assert login_page.is_open(), "Страница логина не загрузилась"

        with allure.step("Ввести валидные креды и нажать войти"):
            login_page.login(
                email=config.test_user_email,
                password=config.test_user_password
            )

        with allure.step("Проверить что открылся дашборд"):
            dashboard_page = DashboardPage(page)
            dashboard_page.unique_element.wait_for(state="visible")
            assert dashboard_page.is_open(), "После логина дашборд не открылся"

        Logger.info("TEST: test_login_success passed")

    @allure.title("Логин с неверным паролем — должна появиться ошибка")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_login_wrong_password(self, page):
        Logger.info("TEST: test_login_wrong_password started")

        with allure.step("Открыть страницу логина"):
            login_page = LoginPage(page)
            login_page.open()

        with allure.step("Ввести неверный пароль и нажать войти"):
            login_page.login(
                email=config.test_user_email,
                password=fake.password()
            )

        with allure.step("Проверить что появился блок с ошибкой"):
            login_page.error_block.wait_for(state="visible")
            assert login_page.is_error_visible(), "Блок с ошибкой не появился"

        Logger.info("TEST: test_login_wrong_password passed")