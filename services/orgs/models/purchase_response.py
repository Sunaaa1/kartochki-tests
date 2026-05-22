from pydantic import BaseModel


class PurchaseResponse(BaseModel):
    creditsPurchased: int
    balanceRubKopecks: int