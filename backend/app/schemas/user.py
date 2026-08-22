from datetime import datetime

from pydantic import BaseModel, ConfigDict


class UserCreate(BaseModel):
    name: str
    email: str
    phone: str
    role: str = "CITIZEN"


class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    phone: str
    role: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)