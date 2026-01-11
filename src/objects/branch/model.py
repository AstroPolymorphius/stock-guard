from sqlalchemy import Column,String,DateTime,ForeignKey
from src.models.base import UUIDModel, TimestampedModel
from uuid import UUID
from sqlalchemy.dialects.postgresql import UUID as pgUUID
from sqlalchemy.orm import Mapped, mapped_column

#Defines a pharmacy branch model
class Branch(UUIDModel, TimestampedModel):
    pharmacy_id: Mapped[UUID] = mapped_column(ForeignKey, nullable=False, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    location: Mapped[str] = mapped_column(String, nullable=False)