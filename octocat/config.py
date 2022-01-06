from pathlib import Path
from typing import NamedTuple

#import pyyaml
from loguru import logger
from pydantic import BaseSettings, Field


cwd = Path(".")
files = [f for f in cwd.glob("*.*")]
if "PosixPath('config.yaml')" in files:
    logger.debug("Found custom config.")
    #custom_config = pyyaml.parse("config.yaml").read()
    #logger.debug("Parsed custom config.")

class OctocatConfig(BaseSettings):
    token: str

    extension_filepath: Path = Path(__file__).parent / "exts"

    class Config:
        env_file = '.env'
        env_prefix = 'OCTOCAT_'

CONFIG = OctocatConfig()

class Roles(NamedTuple):
    administrator: int = 856288946094080000
    moderator: int = 856289049148784640
    helper: int = 857010097913987093    

class Colour(NamedTuple):
    red: int = 0xFF0000
    green: int = 0x00FF00
    blue: int = 0x0000FF
    yellow: int = 0xFFFF00
    purple: int = 0xFF00FF
    cyan: int = 0x00FFFF
    white: int = 0xFFFFFF
    black: int = 0x000000

Color = Colour  # Alias for Americans