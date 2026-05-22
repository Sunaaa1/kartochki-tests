from pydantic import BaseModel
from services.products.models.product_response import ProductResponse


class ProductsListResponse(BaseModel):
    items: list[ProductResponse]
    total: int
    page: int
    limit: int