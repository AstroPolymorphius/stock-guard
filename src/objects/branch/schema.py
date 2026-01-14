from pydantic import BaseModel, ConfigDict
from uuid import UUID
from datetime import datetime
from typing import Optional

class BranchIn(BaseModel):
    name: str
    pharmacy_id: UUID
    location: str

class BranchOut(BranchIn):
    id: UUID
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)