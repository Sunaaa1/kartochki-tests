from services.general.base_service import BaseService
from services.products.helpers.products_helper import ProductsHelper
from services.products.models.product_request import ProductRequest, MarketplaceEnum
from services.products.models.product_response import ProductResponse
from services.products.models.products_list_response import ProductsListResponse
from utils.api_utils import ApiUtils


class ProductsService(BaseService):
    SERVICE_URL = "https://kartochki.store/api"

    def __init__(self, api_utils: ApiUtils):
        super().__init__(api_utils)
        self.products_helper = ProductsHelper(self.api_utils)

    def get_products(self) -> ProductsListResponse:
        response = self.products_helper.get_products()
        response.raise_for_status()
        return ProductsListResponse(**response.json())

    def create_product(self, image_url: str, marketplace: MarketplaceEnum) -> ProductResponse:
        response = self.products_helper.post_product(
            json=ProductRequest(
                imageUrl=image_url,
                marketplace=marketplace
            ).model_dump()
        )
        response.raise_for_status()
        return ProductResponse(**response.json())

    def get_product(self, product_id: str) -> ProductResponse:
        response = self.products_helper.get_product(product_id)
        response.raise_for_status()
        return ProductResponse(**response.json())