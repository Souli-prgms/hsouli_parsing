"""IO module."""
import os.path
from typing import Generator


def open_file(filepath: str) -> Generator[tuple[int, str], None, None]:
    """Open a file and read its content line by line.

    It is a generator so that we can handle large files without occupying too much RAM.

    Args:
        filepath: File local path.

    Yields:
        int: Line index.
        str: Line content.

    """
    if not os.path.exists(filepath):
        raise RuntimeError(f"{filepath} does not exist.")

    with open(filepath, "r", encoding="utf-8") as file:
        for index, line in enumerate(file):
            yield index, line.rstrip()
