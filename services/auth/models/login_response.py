from pydantic import BaseModel
from datetime import datetime


class UserData(BaseModel):
    id: str
    email: str
    name: str
    isAdmin: bool
    createdAt: datetime
    emailVerified: bool
    orgId: str
    orgName: str
    orgPlan: str
    orgCredits: int
    role: str


class LoginResponse(BaseModel):
    token: str
    user: UserData