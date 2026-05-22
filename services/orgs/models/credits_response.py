from pydantic import BaseModel


class CreditsResponse(BaseModel):
    remaining: int
    purchased: int
    used: int
    plan: str
    total: int
    transactions: list