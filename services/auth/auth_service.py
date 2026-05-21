from services.auth.helpers.authorization_helper import AuthorizationHelper
from services.auth.models.login_request import LoginRequest
from services.auth.models.login_response import LoginResponse
from services.auth.models.me_response import MeResponse
from services.general.base_service import BaseService
from utils.api_utils import ApiUtils


class AuthService(BaseService):
    SERVICE_URL = "https://kartochki.store/api"

    def __init__(self, api_utils: ApiUtils):
        super().__init__(api_utils)
        self.authorization_helper = AuthorizationHelper(self.api_utils)

    def login(self, login_request: LoginRequest) -> LoginResponse:
        response = self.authorization_helper.post_login(
            json=login_request.model_dump()
        )
        response.raise_for_status()
        return LoginResponse(**response.json())

    def get_me(self) -> MeResponse:
        response = self.authorization_helper.get_me()
        response.raise_for_status()
        return MeResponse(**response.json())