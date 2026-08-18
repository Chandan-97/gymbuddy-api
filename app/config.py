# app/config.py
import os
from typing import List
from pydantic import AnyHttpUrl, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Pydantic Settings reads variables from environment or a .env file.
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

    # App Settings
    APP_NAME: str = "GymBuddy Sync"
    DEBUG: bool = False
    API_V1_STR: str = "/api/v1"

    # Cryptography & Security
    JWT_SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # Database
    DATABASE_URL: str

    # Example of a Senior-level validator:
    # This automatically formats and validates SQLITE URLs to be async-compatible
    @field_validator("DATABASE_URL", mode="before")
    @classmethod
    def assemble_db_connection(cls, v: str) -> str:
        if v.startswith("sqlite://"):
            # Force the use of the async sqlite driver
            return v.replace("sqlite://", "sqlite+aiosqlite://")
        return v

# Instantiate the settings class.
# This will raise a ValidationError instantly on startup if any required key (like JWT_SECRET_KEY) is missing.
settings = Settings()
