import uuid

from pydantic import BaseModel, UUID4, Field
from datetime import datetime, date
from typing import Optional

    

class Patient(BaseModel):
    """Patient model"""
    id: UUID4
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
    pk: UUID4
    patient_id: UUID4
    drug_code: int
    drug_name: str
    quantity: int
    dosage: int
    start_date: date
    start_datetime: datetime
    end_date: date
    end_datetime: datetime
    
    class Config:
        from_attributes = True
        orm_mode = True

class PatientMedicationPayload(BaseModel):
    """PatientMedication payload model."""
    
    patient_id: UUID4
    drug_name: str = Field(min_lenght=1, max_length=127)
    quantity: int
    dosage: int
    start_date: date
    
