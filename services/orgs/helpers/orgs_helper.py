import requests
from services.general.helpers.base_helper import BaseHelper


class OrgsHelper(BaseHelper):
    ENDPOINT_PREFIX = "/orgs"
    ME_ENDPOINT = f"{ENDPOINT_PREFIX}/me"
    CREDITS_ENDPOINT = f"{ENDPOINT_PREFIX}/credits"
    PURCHASE_ENDPOINT = f"{ENDPOINT_PREFIX}/credits/purchase"
    PLANS_ENDPOINT = f"{ENDPOINT_PREFIX}/plans"
    BALANCE_ENDPOINT = f"{ENDPOINT_PREFIX}/balance"

    def get_me(self) -> requests.Response:
        return self.api_utils.get(self.ME_ENDPOINT)

    def get_credits(self) -> requests.Response:
        return self.api_utils.get(self.CREDITS_ENDPOINT)

    def post_purchase(self, json: dict) -> requests.Response:
        return self.api_utils.post(self.PURCHASE_ENDPOINT, json=json)

    def get_plans(self) -> requests.Response:
        return self.api_utils.get(self.PLANS_ENDPOINT)

    def get_balance(self) -> requests.Response:
        return self.api_utils.get(self.BALANCE_ENDPOINT)
