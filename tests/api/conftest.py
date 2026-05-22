import pytest
from utils.api_utils import ApiUtils
from services.auth.auth_service import AuthService
from services.auth.models.login_request import LoginRequest
from core.config import config
from services.orgs.orgs_service import OrgsService
from services.products.products_service import ProductsService


@pytest.fixture(scope="session")
def api_utils_anon():
    """Неавторизованный клиент"""
    return ApiUtils(url=AuthService.SERVICE_URL)


@pytest.fixture(scope="session")
def auth_token(api_utils_anon):
    """Получаем токен один раз на всю сессию"""
    auth_service = AuthService(api_utils_anon)
    response = auth_service.login(LoginRequest(
        email=config.test_user_email,
        password=config.test_user_password
    ))
    return response.token


@pytest.fixture(scope="session")
def api_utils_auth(auth_token):
    """Авторизованный клиент с токеном"""
    return ApiUtils(
        url=AuthService.SERVICE_URL,
        headers={"Authorization": f"Bearer {auth_token}"}
    )


@pytest.fixture(scope="session")
def auth_service(api_utils_anon):
    return AuthService(api_utils_anon)


@pytest.fixture(scope="session")
def orgs_service(api_utils_auth):
    return OrgsService(api_utils_auth)


@pytest.fixture(scope="session")
def products_service(api_utils_auth):
    return ProductsService(api_utils_auth)


@pytest.fixture(scope="session")
def orgs_service_auth(api_utils_auth):
    from services.orgs.orgs_service import OrgsService
    return OrgsService(api_utils_auth)
