from pathlib import Path
from typing import Generator


def find_extensions() -> Generator[tuple[Path, str], None, None]:
    for path in Path("octocat/exts").rglob("**/*.py"):
        yield path, path_to_module(path)


def path_to_module(path: Path) -> str:
    return f"{(path.parent.as_posix()).replace('/', '.')!s}.{path.stem}"
