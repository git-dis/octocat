"""Octocat is a utility and moderation bot essential for the GitHub Discord server."""
from functools import partial

import loguru


logger = loguru.logger.opt(colors=True)
logger.opt = partial(logger.opt, colours=True)
