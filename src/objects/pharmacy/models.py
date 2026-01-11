from sqlalchemy import Column,String,Integer,DateTime,ForeignKey
from src.models.base import UUIDModel, TimestampedModel
from uuid import UUID
from sqlalchemy.dialects.postgresql import UUID as pgUUID
from sqlalchemy.orm import Mapped, mapped_column

#Defines a pharmacy model
class Pharmacy(UUIDModel, TimestampedModel):
    __table__ = "Pharmacies"
    name: Mapped[str] = mapped_column(String, nullable=False)