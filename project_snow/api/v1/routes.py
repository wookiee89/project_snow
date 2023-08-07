import uuid

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from project_snow.api import models
from project_snow.database import models as db_models
from project_snow.database.session import get_db_session

router = APIRouter(prefix="/v1", tags=["v1"])

@router.post("/PatientMedication", status_code=status.HTTP_201_CREATED)
async def create_patient_medication(
    data: models.PatientMedicationPayload,
    session: AsyncSession = Depends(get_db_session),
) -> models.PatientMedication:
    patient_medication = db_models.PatientMedication(**data.model_dump())
    session.add(patient_medication)
    await session.commit()
    await session.refresh(patient_medication)
    return models.Ingredient.from_orm(patient_medication)