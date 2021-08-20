"""Configuration file for Octocat."""
from pydantic import BaseSettings, BaseModel 


class Colour(BaseModel):
    """Dataclass of colours for Octocat."""

    primary: int = 0xf34f29    # Git orange
    secondary: int = 0xffffff  # White
    success: int = 0x2ecc71    # Light green
    warning: int = 0xf1c40f    # Strong yellow
    danger: int = 0xe74c3c     # Strong red


class Settings(BaseSettings):
    """Configuration for Octocat."""

    token: str
    prefix: str = "!"

    colour: Colour = Colour()

    class Config:
        """Reads configuration secrets from .env file."""

        env_file = ".env"
        env_prefix = "OCTOCAT_"
        case_sensitive = False


CONFIG = Settings()

