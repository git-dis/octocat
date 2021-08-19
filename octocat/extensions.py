"""Enables Octocat to dynamically load extension cogs."""
from pathlib import Path
from typing import Generator


def find_extensions() -> Generator[tuple[Path, str], None, None]:
    """Find extensions in the extensions directory."""
    for path in Path("octocat/exts").rglob("**/*.py"):
        yield path, path_to_module(path)


def path_to_module(path: Path) -> str:
    """Convert extension path into a module that can be used to load the extension."""
    return f"{(path.parent.as_posix()).replace('/', '.')!s}.{path.stem}"
