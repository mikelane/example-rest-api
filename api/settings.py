"""Settings for the application."""
from __future__ import annotations

from pydantic import (
    BaseSettings,
    Field,
)


class Settings(BaseSettings):
    """Settings for the application."""

    class Config:
        env_file = '.env.local', '.env.test', '.env.qa', '.env.prod'
        encodings = 'utf-8'

    debug: bool = Field(default=False)


settings = Settings()
