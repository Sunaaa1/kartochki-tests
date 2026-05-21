import requests
from services.general.helpers.base_helper import BaseHelper


class AuthorizationHelper(BaseHelper):
    ENDPOINT_PREFIX = "/auth"
    LOGIN_ENDPOINT = f"{ENDPOINT_PREFIX}/login"
    ME_ENDPOINT = f"{ENDPOINT_PREFIX}/me"

    def post_login(self, json: dict) -> requests.Response:
        return self.api_utils.post(self.LOGIN_ENDPOINT, json=json)

    def get_me(self) -> requests.Response:
        return self.api_utils.get(self.ME_ENDPOINT)