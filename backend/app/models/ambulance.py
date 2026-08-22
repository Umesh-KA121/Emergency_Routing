from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.connection import Base


class Ambulance(Base):
    __tablename__ = "ambulances"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    vehicle_number: Mapped[str] = mapped_column(
        String(30),
        unique=True
    )

    status: Mapped[str] = mapped_column(
        String(30),
        default="AVAILABLE"
    )

    latitude: Mapped[float]
    longitude: Mapped[float]

    capacity: Mapped[int] = mapped_column(
        default=1
    )

    routes = relationship(
        "Route",
        back_populates="ambulance"
    )