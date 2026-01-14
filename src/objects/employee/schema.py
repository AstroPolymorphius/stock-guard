from pydantic import BaseModel, ConfigDict
from uuid import UUID
from datetime import datetime
from typing import Optional

class EmployeeIn(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str
    branch_id: UUID
    role: str
    
class EmployeeOut(BaseModel):
    id: UUID
    first_name: str
    last_name: str
    email: str
    branch_id: UUID
    role: str
    created_at: datetime