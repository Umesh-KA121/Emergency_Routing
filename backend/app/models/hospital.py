from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.connection import Base


class Hospital(Base):
    __tablename__ = "hospitals"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    name: Mapped[str] = mapped_column(
        String(150)
    )

    latitude: Mapped[float]
    longitude: Mapped[float]

    available_beds: Mapped[int] = mapped_column(
        default=0
    )

    emergency_capacity: Mapped[int] = mapped_column(
        default=0
    )

    status: Mapped[str] = mapped_column(
        String(30),
        default="AVAILABLE"
    )