from typing import TYPE_CHECKING
from datetime import date
from sqlalchemy import Column,String,Integer,ForeignKey,Date
from src.models.base import UUIDModel, TimestampedModel
from uuid import UUID
from sqlalchemy.dialects.postgresql import UUID as pgUUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from src.objects.product.model import Product
#Defines a drug batch model
class Batch(UUIDModel, TimestampedModel):
    __table__ = "batches"
    product_id: Mapped[UUID] = mapped_column(ForeignKey, nullable=False, index=True)
    batch_number: Mapped[str] = mapped_column(String, nullable=False, index=True)
    branch_id: Mapped[UUID] = mapped_column(ForeignKey, nullable=False, index=True)
    current_qty: Mapped[int] = mapped_column(Integer, default=0)
    expiry_date: Mapped[date] = mapped_column(Date, nullable=False, index=True)
    #Establishing relationship between product and batch table
    product: Mapped["Product"] = relationship("Product", back_populates="batches")