from pydantic import BaseModel, Field, ConfigDict, FutureDate
from uuid import UUID
from datetime import datetime
from typing import Optional

class BatchIn(BaseModel):
    product_id: UUID
    batch_number: str
    branch_id: UUID
    current_qty: int = Field(default=1,examples=["5"])
    expiry_date: FutureDate

class BatchOut(BatchIn):
    id: UUID
    updated_at: datetime
    
    model_config = ConfigDict(from_attributes=True)