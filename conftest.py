import pytest
from playwright.sync_api import sync_playwright, Browser, BrowserContext, Page
from core.config import config
from core.logger import Logger


@pytest.fixture(scope="session")
def browser_instance():
    """Запускает браузер один раз на всю сессию тестов"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=config.headless)
        Logger.info("Browser launched")
        yield browser
        browser.close()
        Logger.info("Browser closed")


@pytest.fixture(scope="function")
def context(browser_instance: Browser):
    """Чистый контекст для каждого теста — как новая вкладка инкогнито"""
    ctx = browser_instance.new_context(
        base_url=config.base_url,
        viewport={"width": 1920, "height": 1080},
    )
    Logger.info("New browser context created")
    yield ctx
    ctx.close()
    Logger.info("Browser context closed")


@pytest.fixture(scope="function")
def page(context: BrowserContext):
    """Страница браузера — передаётся в каждый тест"""
    p = context.new_page()
    p.set_default_timeout(config.timeout)
    Logger.info("New page created")
    yield p
    p.close()
    Logger.info("Page closed")


@pytest.fixture(scope="function")
def auth_page(context: BrowserContext):
    """Страница с уже залогиненным пользователем через localStorage"""
    import json

    p = context.new_page()
    p.set_default_timeout(config.timeout)

    # Открываем сайт чтобы установить localStorage
    p.goto("/")

    # Делаем логин через API чтобы получить токен
    import requests
    response = requests.post(
        f"{config.api_url}/auth/login",
        json={
            "email": config.test_user_email,
            "password": config.test_user_password
        }
    )
    response.raise_for_status()
    token = response.json().get("accessToken")

    # Кладём токен в localStorage — как это делает само приложение
    p.evaluate(f"localStorage.setItem('token', '{token}')")
    p.reload()

    Logger.info(f"Authenticated as {config.test_user_email}")
    yield p
    p.close()