import requests
from services.general.helpers.base_helper import BaseHelper


class OrgsHelper(BaseHelper):
    ENDPOINT_PREFIX = "/orgs"
    ME_ENDPOINT = f"{ENDPOINT_PREFIX}/me"
    CREDITS_ENDPOINT = f"{ENDPOINT_PREFIX}/credits"

    def get_me(self) -> requests.Response:
        return self.api_utils.get(self.ME_ENDPOINT)

    def get_credits(self) -> requests.Response:
        return self.api_utils.get(self.CREDITS_ENDPOINT)