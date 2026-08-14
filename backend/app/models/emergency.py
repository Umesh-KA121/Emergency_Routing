from datetime import datetime

from sqlalchemy import ForeignKey, String, Text, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from app.database.connection import Base


class Emergency(Base):
    __tablename__ = "emergencies"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )

    description: Mapped[str] = mapped_column(Text)

    latitude: Mapped[float]
    longitude: Mapped[float]

    severity: Mapped[str] = mapped_column(
        String(20),
        default="PENDING"
    )

    status: Mapped[str] = mapped_column(
        String(30),
        default="PENDING"
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )