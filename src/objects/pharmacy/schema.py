from pydantic import BaseModel, ConfigDict
from uuid import UUID
from datetime import datetime
from typing import Optional

class PharmacyIn(BaseModel):
    name: str

class PharmacyOut(PharmacyIn):
    id: UUID
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)