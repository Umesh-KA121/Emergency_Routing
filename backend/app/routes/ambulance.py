from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.models.ambulance import Ambulance
from app.schemas.ambulance import (
    AmbulanceCreate,
    AmbulanceResponse
)


router = APIRouter(
    prefix="/ambulances",
    tags=["Ambulances"]
)


@router.post("/", response_model=AmbulanceResponse)
def create_ambulance(
    ambulance: AmbulanceCreate,
    db: Session = Depends(get_db)
):
    existing = (
        db.query(Ambulance)
        .filter(
            Ambulance.vehicle_number
            == ambulance.vehicle_number
        )
        .first()
    )

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Vehicle number already exists"
        )

    new_ambulance = Ambulance(
        vehicle_number=ambulance.vehicle_number,
        latitude=ambulance.latitude,
        longitude=ambulance.longitude,
        capacity=ambulance.capacity,
        status=ambulance.status
    )

    db.add(new_ambulance)
    db.commit()
    db.refresh(new_ambulance)

    return new_ambulance


@router.get("/", response_model=list[AmbulanceResponse])
def get_ambulances(
    db: Session = Depends(get_db)
):
    return db.query(Ambulance).all()


@router.get(
    "/{ambulance_id}",
    response_model=AmbulanceResponse
)
def get_ambulance(
    ambulance_id: int,
    db: Session = Depends(get_db)
):
    ambulance = (
        db.query(Ambulance)
        .filter(Ambulance.id == ambulance_id)
        .first()
    )

    if not ambulance:
        raise HTTPException(
            status_code=404,
            detail="Ambulance not found"
        )

    return ambulance