from pydantic import BaseModel, ConfigDict


class HospitalCreate(BaseModel):
    name: str
    latitude: float
    longitude: float
    available_beds: int = 0
    emergency_capacity: int = 0
    status: str = "AVAILABLE"


class HospitalResponse(BaseModel):
    id: int
    name: str
    latitude: float
    longitude: float
    available_beds: int
    emergency_capacity: int
    status: str

    model_config = ConfigDict(from_attributes=True)