from typing import List,TYPE_CHECKING
from sqlalchemy import Column,String,DateTime,ForeignKey
from src.models.base import UUIDModel, TimestampedModel
from uuid import UUID
from sqlalchemy.dialects.postgresql import UUID as pgUUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from src.objects.pharmacy.model import Pharmacy
    from src.objects.employee.model import Employee
    from src.objects.batch.model import Batch
    
#Defines a pharmacy branch model
class Branch(UUIDModel, TimestampedModel):
    __tablename__ = "branches"
    pharmacy_id: Mapped[UUID] = mapped_column(ForeignKey("pharmacies.id"), nullable=False, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    location: Mapped[str] = mapped_column(String, nullable=False)
    ##Establishing the relationship between pharmacy and branch models here in the child model
    pharmacy: Mapped["Pharmacy"] = relationship("Pharmacy", back_populates="branches")
    #Establishing the relationship between branch and employee models here in the parent model
    employees: Mapped[List["Employee"]] = relationship(back_populates="branch")
    #Establishing the relationship between branch and batch models here in the parent model
    batches: Mapped[List["Batch"]] = relationship(back_populates="branch")