from pydantic import BaseModel, ConfigDict
from uuid import UUID
from datetime import datetime
from typing import Optional

class InventoryTransactionIn():
    batch_id: UUID
    type: str
    qty_change: int
    employee_id: UUID

class InventoryTransactionOut(InventoryTransactionIn):
    id: UUID
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)