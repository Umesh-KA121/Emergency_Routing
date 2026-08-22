from datetime import datetime

from pydantic import BaseModel, ConfigDict


class EmergencyCreate(BaseModel):
    user_id: int
    description: str
    latitude: float
    longitude: float


class EmergencyResponse(BaseModel):
    id: int
    user_id: int
    description: str
    latitude: float
    longitude: float
    severity: str
    status: str
    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )