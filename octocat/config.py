"""Configuration file for Octocat."""
from pydantic import BaseSettings


class Settings(BaseSettings):
    """Configuration for Octocat."""

    token: str
    prefix: str = "!"

    class Config:
        """Reads configuration secrets from .env file."""

        env_file = ".env"
        env_prefix = "OCTOCAT_"
        case_sensitive = False


CONFIG = Settings()
