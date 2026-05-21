from pydantic import BaseModel
from datetime import datetime


class OrgResponse(BaseModel):
    id: str
    name: str
    slug: str
    plan: str
    creditsRemaining: int
    creditsPurchased: int
    creditsUsed: int
    balanceUsdCents: int
    balanceRubKopecks: int
    createdAt: datetime
    updatedAt: datetime