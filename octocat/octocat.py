from datetime import datetime
import os

from disnake import Intents
from disnake.ext import commands
from loguru import logger

from octocat.config import CONFIG

class Octocat(commands.Bot):
    """The core of Octocat"""

    def __init__(self) -> None:
        intents = Intents.default()

        super().__init__(
            intents=intents,
            sync_commands_debug=True,
            test_guilds=[
                792953183630655509,
            ],
        )

        self.loop.create_task(self.setup())

        self.launch_time = datetime.utcnow().timestamp()

    async def setup(self) -> None:
        self.load_extensions()

    def load_extensions(self) -> None:
        logger.info("Starting to load extensions...")
        # TODO: Load extensions
        # for extension in CONFIG.extension_filepath.rglob("*.py"):
        #     if extension.name.startswith("_"):
        #         continue
        #     qualified_name = f"octocat.exts.{extension.}"
        #     self.load_extension(qualified_name)
        #     logger.info(f"Loaded extension {qualified_name}")
        self.load_extension("octocat.exts.utils.status")
        self.load_extension("octocat.exts.utils.colour")
        logger.success("Loaded all extensions successfully")

    def run(self) -> None:
        """Runs the bot with the token specified in the configuration."""
        logger.info("Starting Octocat...")

        super().run(CONFIG.token)

    async def close(self) -> None:
        """Closes Octocat."""
        logger.info("Closing Octocat...")

        await super().close()