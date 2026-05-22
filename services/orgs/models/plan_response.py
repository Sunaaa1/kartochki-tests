from pydantic import BaseModel
from typing import Optional


class PlanResponse(BaseModel):
    id: str
    monthly: int
    priceRub: int
    name: str
    features: list[str]
    credits: int