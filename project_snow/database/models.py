import uuid

from sqlalchemy import Column, Date, DateTime, ForeignKey, Integer, String, func, orm
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

BaseModel = declarative_base()


class Base(BaseModel):
    __abstract__ = True  # This ensures that Base class doesn't map to any table

    pk: orm.Mapped[uuid.UUID] = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    created_at: orm.Mapped[DateTime] = Column(DateTime(timezone=True), server_default=func.now())
    updated_at: orm.Mapped[DateTime] = Column(DateTime(timezone=True), onupdate=func.now())


class Patient(Base):
    __tablename__ = "patients"

    first_name: orm.Mapped[str] = Column(String, nullable=False)
    last_name: orm.Mapped[str] = Column(String, nullable=False)
    phone_number: orm.Mapped[str] = Column(String, nullable=False)

    medications: orm.Mapped[relationship] = relationship("PatientMedication", back_populates="patient")


class PatientMedication(Base):
    __tablename__ = "patient_medications"

    patient_id: orm.Mapped[UUID] = Column(UUID(as_uuid=True), ForeignKey("patients.pk"), nullable=False)
    drug_code: orm.Mapped[int] = Column(Integer, nullable=False)
    drug_name: orm.Mapped[str] = Column(String, nullable=False)
    quantity: orm.Mapped[int] = Column(Integer, nullable=False)
    refills: orm.Mapped[int] = Column(Integer, nullable=True)
    dosage: orm.Mapped[int] = Column(Integer, nullable=False)
    start_date: orm.Mapped[Date] = Column(Date, nullable=False)
    start_datetime: orm.Mapped[DateTime] = Column(DateTime, nullable=False)
    end_date: orm.Mapped[Date] = Column(Date, nullable=False)
    end_datetime: orm.Mapped[DateTime] = Column(DateTime, nullable=False)

    patient: orm.Mapped[relationship] = relationship("Patient", back_populates="medications")