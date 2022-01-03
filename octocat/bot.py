"""Module containing core bot base for Octocat."""
from typing import Any

from disnake.ext import commands
from disnake.ext.commands import Bot

from octocat import logger
from octocat.config import CONFIG
from octocat.extensions import find_extensions


class Octocat(Bot):
    """Core bot class for Octocat."""

    def __init__(self, *args: list[Any], **kwargs: dict[str, Any]) -> None:
        config = {
            "command_prefix": commands.when_mentioned_or(CONFIG.prefix),
            "case_insensitive": True
        }

        kwargs.update(config)

        super().__init__(*args, **kwargs)

    async def on_ready(self) -> None:
        """Load all extensions."""
        logger.info(f"Logged in <red>{self.user}</>")

        for path, extension in find_extensions():
            logger.info(f"Loading extension <magenta>{path.stem}</> from <magenta>{path.parent}</>")

            # noinspection PyBroadException
            try:
                self.load_extension(extension)
            except Exception:
                logger.exception(
                    f"Failed to load extension <magenta>{path.stem}</> "
                    f"from <magenta>{path.parent}</>",
                )
            else:
                logger.info(f"Loaded extension <magenta>{path.stem}</> from <magenta>{path.parent}</>")
