from sqlalchemy import Column,String,DateTime,ForeignKey
from src.models.base import UUIDModel, TimestampedModel
from uuid import UUID
from sqlalchemy.dialects.postgresql import UUID as pgUUID
from sqlalchemy.orm import Mapped, mapped_column

#Defines an employee model
class Employee(UUIDModel, TimestampedModel):
    first_name: Mapped[str] = mapped_column(String, nullable=False)
    last_name: Mapped[str] = mapped_column(String, nullable=False)
    branch_id: Mapped[UUID] = mapped_column(ForeignKey, nullable=False, index=True)
    email: Mapped[str] = mapped_column(String, nullable=False, index=True)
    password: Mapped[str] = mapped_column(String, nullable=False)
    role: Mapped[str] = mapped_column(String, nullable=False, index=True)