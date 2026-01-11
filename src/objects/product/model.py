from sqlalchemy import Column,String,Integer,DateTime,ForeignKey
from src.models.base import UUIDModel, TimestampedModel
from uuid import UUID
from sqlalchemy.dialects.postgresql import UUID as pgUUID
from sqlalchemy.orm import Mapped, mapped_column

#Defines a drug product model
class Product(UUIDModel, TimestampedModel):
    name: Mapped[str] = mapped_column(String, nullable=False, index=True)
    generic_name: Mapped[str] = mapped_column(String, nullable=True)
    request_unit: Mapped[str] = mapped_column(String, nullable=False)
    base_unit: Mapped[str] = mapped_column(String, nullable=False)
    conversion_factor: Mapped[int] = mapped_column(Integer, default=0)
    min_safety_stock: Mapped[int] = mapped_column(Integer, default=10)