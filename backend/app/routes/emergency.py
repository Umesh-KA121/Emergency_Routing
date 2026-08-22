from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.models.emergency import Emergency
from app.models.user import User
from app.schemas.emergency import (
    EmergencyCreate,
    EmergencyResponse
)


router = APIRouter(
    prefix="/emergencies",
    tags=["Emergencies"]
)


@router.post("/", response_model=EmergencyResponse)
def create_emergency(
    emergency: EmergencyCreate,
    db: Session = Depends(get_db)
):
    user = (
        db.query(User)
        .filter(User.id == emergency.user_id)
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    new_emergency = Emergency(
        user_id=emergency.user_id,
        description=emergency.description,
        latitude=emergency.latitude,
        longitude=emergency.longitude
    )

    db.add(new_emergency)
    db.commit()
    db.refresh(new_emergency)

    return new_emergency


@router.get("/", response_model=list[EmergencyResponse])
def get_emergencies(
    db: Session = Depends(get_db)
):
    return db.query(Emergency).all()


@router.get("/{emergency_id}", response_model=EmergencyResponse)
def get_emergency(
    emergency_id: int,
    db: Session = Depends(get_db)
):
    emergency = (
        db.query(Emergency)
        .filter(Emergency.id == emergency_id)
        .first()
    )

    if not emergency:
        raise HTTPException(
            status_code=404,
            detail="Emergency not found"
        )

    return emergency