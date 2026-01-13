from typing import TYPE_CHECKING
from datetime import date
from sqlalchemy import Column,String,Integer,DateTime,ForeignKey, Date
from src.models.base import UUIDModel, TimestampedModel
from uuid import UUID
from sqlalchemy.dialects.postgresql import UUID as pgUUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from src.objects.batch.model import Batch
    from src.objects.employee.model import Employee

#Defines an inventory transaction model
class InventoryTransaction(UUIDModel, TimestampedModel):
    batch_id: Mapped[UUID] = mapped_column(ForeignKey("batches.id"), nullable=False, index=True)
    type: Mapped[str] = mapped_column(String, nullable=False, index=True)
    qty_change: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    created_at: Mapped[date] = mapped_column(Date, nullable=False, index=True)
    employee_id: Mapped[UUID] = mapped_column(ForeignKey("employees.id"), nullable=False, index=True)
    #Establishing the relationship between batch and inventorytransaction models here in the child model
    batch: Mapped["Batch"] = relationship("Batch", back_populates="inventory_transactions")
    #Establishing relationship between employee and inventorytransaction models here in the child model
    employee: Mapped["Employee"] = relationship("Employee", back_populates="inventory_transactions")