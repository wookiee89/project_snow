import logging

from functools import lru_cache
from pydantic_settings import BaseSettings

logging.basicConfig(level=logging.INFO)


class Settings(BaseSettings):
    """
    Settings for the FastAPI server.
    Based on pydantic BaseSettings - powerful tool autoload the .env file in the background.
    """
    # AUTH0 configuration    
    AUTH0_DOMAIN: str
    AUTH0_ALGORITHMS: str = "RS256"
    AUTH0_DEFAULT_DB_CONNECTION: str = "Username-Password-Authentication"
    AUTH0_API_DEFAULT_AUDIENCE: str
    AUTH0_APPLICATION_CLIENT_ID: str
    AUTH0_APPLICATION_CLIENT_SECRET: str
    AUTH0_TEST_USERNAME: str
    AUTH0_TEST_PASSWORD: str
    # Management API
    AUTH0_MANAGEMENT_API_CLIENT_ID: str
    AUTH0_MANAGEMENT_API_CLIENT_SECRET: str
    AUTH0_MANAGEMENT_API_AUDIENCE: str

    PROJECT_NAME: str = "project_snow"
    DEBUG: bool = False
    ENVIRONMENT: str = "local"

    # Database
    DATABASE_URL: str = ""

    class Config:
        env_file = ".env"
        case_sensitive = True

@lru_cache()
def get_settings(**kwargs) -> Settings:
    """
    Get settings. ready for FastAPI's Depends.
    lru_cache - cache the Settings object per arguments given.
    """
    settings = Settings(**kwargs)
    return settings