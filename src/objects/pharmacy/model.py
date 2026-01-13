from typing import List,TYPE_CHECKING
from sqlalchemy import Column,String,Integer,DateTime,ForeignKey
from src.models.base import UUIDModel, TimestampedModel
from uuid import UUID
from sqlalchemy.dialects.postgresql import UUID as pgUUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from src.objects.branch.model import Branch
#Defines a pharmacy model
class Pharmacy(UUIDModel, TimestampedModel):
    __tablename__ = "pharmacies"
    name: Mapped[str] = mapped_column(String, nullable=False)
    #Establishing relationship between pharmacy and branch models here in the parent model
    branches: Mapped[List["Branch"]] = relationship(back_populates="pharmacy")