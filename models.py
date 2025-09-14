from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

# Base model of an employee with shared fields
class EmployeeBase(BaseModel):
    name: str = Field(min_length=2, max_length=100, description="Vollständiger Name")
    email: EmailStr = Field(description="Gültige Email-Adresse")
    position: Optional[str] = Field(None, max_length=100, description="Position/Rolle")
    start_date: Optional[datetime] = Field(None, description="Startdatum")
    # salary: Optional[float] = Field(None, ge=0)

# Creating an employee with all field
class EmployeeCreate(EmployeeBase):
    salary: Optional[float] = Field(None, ge=0, description="Gehalt (Optional)")

# Updates (all fields are optional)
class EmployeeUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=100)
    email: Optional[EmailStr] = None
    position: Optional[str] = Field(None, max_length=100)
    salary: Optional[float] = Field(None, ge=0)
# API responses (we will NOT hide the salary)
class Employee(EmployeeBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True



