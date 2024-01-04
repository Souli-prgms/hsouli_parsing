"""Logger module."""
from typing import ClassVar
import logging

logging.basicConfig(level=logging.INFO)


class _TestLogger(logging.Logger):
    """Test logger class.

    Could be a singleton if we only wanted one unique instance.
    Could also be modified to create a log file at each run.
    """

    _fmt: ClassVar[str] = "%(message)s"

    def __init__(self, name: str = "parsing_assignment") -> None:
        """Constructs a logger class.

        Args:
            name: Logger name.

        """
        super().__init__(name)
        self._handler = logging.StreamHandler()
        self._handler.setLevel(logging.INFO)
        self._formatter = logging.Formatter(self._fmt)
        self._handler.setFormatter(self._formatter)
        self.addHandler(self._handler)

    def output(self, line_index: int, msg: str) -> None:
        """Log formatted line data to console.

        Args:
            line_index: Line index.
            msg: New line data.

        """
        self.info("%i : %s", line_index, msg)


logger = _TestLogger()
