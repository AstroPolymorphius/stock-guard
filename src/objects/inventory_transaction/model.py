from datetime import date
from sqlalchemy import Column,String,Integer,DateTime,ForeignKey, Date
from src.models.base import UUIDModel, TimestampedModel
from uuid import UUID
from sqlalchemy.dialects.postgresql import UUID as pgUUID
from sqlalchemy.orm import Mapped, mapped_column

#Defines an inventory transaction model
class Inventory_Transaction(UUIDModel, TimestampedModel):
    __table__ = "Inventory_Transactions"
    batch_id: Mapped[UUID] = mapped_column(ForeignKey, nullable=False, index=True)
    type: Mapped[str] = mapped_column(String, nullable=False, index=True)
    qty_change: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    created_at: Mapped[date] = mapped_column(Date, nullable=False, index=True)
    employee_id: Mapped[UUID] = mapped_column(ForeignKey, nullable=False, index=True)