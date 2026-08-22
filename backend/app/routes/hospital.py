from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.models.hospital import Hospital
from app.schemas.hospital import (
    HospitalCreate,
    HospitalResponse
)


router = APIRouter(
    prefix="/hospitals",
    tags=["Hospitals"]
)


@router.post("/", response_model=HospitalResponse)
def create_hospital(
    hospital: HospitalCreate,
    db: Session = Depends(get_db)
):
    new_hospital = Hospital(
        name=hospital.name,
        latitude=hospital.latitude,
        longitude=hospital.longitude,
        available_beds=hospital.available_beds,
        emergency_capacity=hospital.emergency_capacity,
        status=hospital.status
    )

    db.add(new_hospital)
    db.commit()
    db.refresh(new_hospital)

    return new_hospital


@router.get("/", response_model=list[HospitalResponse])
def get_hospitals(
    db: Session = Depends(get_db)
):
    return db.query(Hospital).all()


@router.get(
    "/{hospital_id}",
    response_model=HospitalResponse
)
def get_hospital(
    hospital_id: int,
    db: Session = Depends(get_db)
):
    hospital = (
        db.query(Hospital)
        .filter(Hospital.id == hospital_id)
        .first()
    )

    if not hospital:
        raise HTTPException(
            status_code=404,
            detail="Hospital not found"
        )

    return hospital