from datetime import datetime

from sqlalchemy import ForeignKey, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.connection import Base


class Route(Base):
    __tablename__ = "routes"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    emergency_id: Mapped[int] = mapped_column(
        ForeignKey("emergencies.id")
    )

    ambulance_id: Mapped[int] = mapped_column(
        ForeignKey("ambulances.id")
    )

    hospital_id: Mapped[int] = mapped_column(
        ForeignKey("hospitals.id")
    )

    distance: Mapped[float]

    estimated_time: Mapped[float]

    algorithm: Mapped[str] = mapped_column(
        String(30)
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    emergency = relationship(
        "Emergency",
        back_populates="routes"
    )

    ambulance = relationship(
        "Ambulance",
        back_populates="routes"
    )

    hospital = relationship(
        "Hospital",
        back_populates="routes"
    )