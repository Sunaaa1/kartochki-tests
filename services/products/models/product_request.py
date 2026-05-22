from pydantic import BaseModel, ConfigDict
from typing import Optional
from enum import StrEnum


class MarketplaceEnum(StrEnum):
    WILDBERRIES = "wildberries"
    OZON = "ozon"
    AMAZON = "amazon"
    SHOPIFY = "shopify"


class ProductRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    imageUrl: str
    marketplace: MarketplaceEnum