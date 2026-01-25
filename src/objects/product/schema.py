from pydantic import BaseModel, ConfigDict
from uuid import UUID
from datetime import datetime
from typing import Optional


class ProductIn(BaseModel):
    name: str
    generic_name: Optional[str] = None
    gtin: Optional[str] = None
    request_unit: str
    base_unit: str
    conversion_factor: int = 1
    min_safety_stock: int = 0

class ProductOut(ProductIn):
    id: UUID
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)