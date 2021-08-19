"""Starts up the Octocat bot."""
from octocat import logger
from octocat.bot import Octocat
from octocat.config import CONFIG


@logger.catch()
def start() -> None:
    """Entrypoint for Octocat."""
    octocat = Octocat()
    octocat.run(CONFIG.token)


if __name__ == "__main__":
    start()
