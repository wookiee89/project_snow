import logging

from pydantic_settings import BaseSettings

logging.basicConfig(level=logging.INFO)


class Settings(BaseSettings):
    """App settings."""

    PROJECT_NAME: str = "project_snow"
    DEBUG: bool = False
    ENVIRONMENT: str = "local"

    # Database
    DATABASE_URL: str = ""

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()