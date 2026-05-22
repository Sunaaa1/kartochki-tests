import requests
from services.general.helpers.base_helper import BaseHelper


class ProductsHelper(BaseHelper):
    ENDPOINT_PREFIX = "/products"

    def get_products(self, **kwargs) -> requests.Response:
        return self.api_utils.get(self.ENDPOINT_PREFIX, **kwargs)

    def post_product(self, json: dict) -> requests.Response:
        return self.api_utils.post(self.ENDPOINT_PREFIX, json=json)

    def get_product(self, product_id: str) -> requests.Response:
        return self.api_utils.get(f"{self.ENDPOINT_PREFIX}/{product_id}")