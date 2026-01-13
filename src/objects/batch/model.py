from typing import List,TYPE_CHECKING
from datetime import date
from sqlalchemy import Column,String,Integer,ForeignKey,Date
from src.models.base import UUIDModel, TimestampedModel
from uuid import UUID
from sqlalchemy.dialects.postgresql import UUID as pgUUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from src.objects.product.model import Product
    from src.objects.inventory_transaction.model import InventoryTransaction
    from src.objects.branch.model import Branch

#Defines a drug batch model
class Batch(UUIDModel, TimestampedModel):
    __tablename__ = "batches"
    product_id: Mapped[UUID] = mapped_column(ForeignKey("products.id"), nullable=False, index=True)
    batch_number: Mapped[str] = mapped_column(String, nullable=False, index=True)
    branch_id: Mapped[UUID] = mapped_column(ForeignKey("branches.id"), nullable=False, index=True)
    current_qty: Mapped[int] = mapped_column(Integer, default=0)
    expiry_date: Mapped[date] = mapped_column(Date, nullable=False, index=True)
    #Establishing relationship between product and batch models here in the child model
    product: Mapped["Product"] = relationship("Product", back_populates="batches")
    #Establishing relationship between batch and inventorytransaction models here in the parent model
    inventory_transactions: Mapped[List["InventoryTransaction"]] = relationship(back_populates="batch")
    #Establishing relationship between branch and batch models here in the child model
    branch: Mapped["Product"] = relationship("Product", back_populates="batches")
