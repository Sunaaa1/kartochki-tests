from pydantic import BaseModel, ConfigDict


class PurchaseRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    credits: int
    amountRubKopecks: int