from octocat import logger
from octocat.bot import Octocat
from octocat.config import CONFIG


@logger.catch()
def start() -> None:
    octocat = Octocat()
    octocat.run(CONFIG.token)


if __name__ == "__main__":
    start()