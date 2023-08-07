import uuid

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from project_snow.api import models
from project_snow.database import models as db_models
from project_snow.database.session import get_db_session

router = APIRouter(prefix="/v1", tags=["v1"])


@router.post("/ingredients", status_code=status.HTTP_201_CREATED)
async def create_ingredient(
    data: models.IngredientPayload,
    session: AsyncSession = Depends(get_db_session),
) -> models.Ingredient:
    ingredient = db_models.Ingredient(**data.model_dump())
    session.add(ingredient)
    await session.commit()
    await session.refresh(ingredient)
    return models.Ingredient.from_orm(ingredient)


@router.get("/ingredients", status_code=status.HTTP_200_OK)
async def get_ingredients(
    session: AsyncSession = Depends(get_db_session),
) -> list[models.Ingredient]:
    ingredients = await session.scalars(select(db_models.Ingredient))
    return [models.Ingredient.from_orm(ingredient) for ingredient in ingredients]


@router.get("/ingredients/{pk}", status_code=status.HTTP_200_OK)
async def get_ingredient(
    pk: uuid.UUID,
    session: AsyncSession = Depends(get_db_session),
) -> models.Ingredient:
    ingredient = await session.get(db_models.Ingredient, pk)
    if ingredient is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Ingredient does not exist",
        )
    return models.Ingredient.from_orm(ingredient)