from pydantic import BaseModel, ConfigDict


class AmbulanceCreate(BaseModel):
    vehicle_number: str
    latitude: float
    longitude: float
    capacity: int = 1
    status: str = "AVAILABLE"


class AmbulanceResponse(BaseModel):
    id: int
    vehicle_number: str
    status: str
    latitude: float
    longitude: float
    capacity: int

    model_config = ConfigDict(from_attributes=True)