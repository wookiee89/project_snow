import uuid

from pydantic import BaseModel, Field
from datetime import datetime, date
from typing import Optional

    

class Patient(BaseModel):
    """Patient model"""
    id: uuid
    first_name: str
    last_name: str
    phone_number: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
        orm_mode = True


class PatientMedication(BaseModel):
    """PatientMedication model"""
    pk: uuid
    patient_id: uuid
    drug_code: int
    drug_name: str
    quantity: int
    refills: Optional[int] = None
    dosage: int
    start_date: date
    start_datetime: datetime
    end_date: date
    end_datetime: datetime
    
    class Config:
        from_attributes = True
        orm_mode = True
