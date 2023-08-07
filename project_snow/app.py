from fastapi import FastAPI

from project_snow.api.v1.routes import router as v1_router
# from project_snow.api.v2.routes import router as v2_router
from project_snow.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    docs_url="/api/docs",
    openapi_url="/api/openapi.json",
)

app.include_router(v1_router, prefix="/api")
# app.include_router(v2_router, prefix="/api")