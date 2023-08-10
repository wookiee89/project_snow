import typing
from datetime import date, datetime

from pydantic import UUID4, AnyUrl, BaseModel, EmailStr, Field

from project_snow.core.config import Settings, get_settings

settings: Settings = get_settings()

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

class CreateUser(BaseModel):
    connection: str = settings.AUTH0_DEFAULT_DB_CONNECTION
    email: EmailStr
    password: str
    name: str
    verify_email: bool = False  # Whether the user will receive a verification email after creation (true) or no email (false). Overrides behavior of email_verified parameter.
    email_verified: typing.Optional[
        bool
    ] = False  # Whether this email address is verified (true) or unverified (false). User will receive a verification email after creation if email_verified is false or not specified
    given_name: typing.Optional[str] = None
    family_name: typing.Optional[str] = None
    nickname: typing.Optional[str] = None
    picture: typing.Optional[AnyUrl] = None
