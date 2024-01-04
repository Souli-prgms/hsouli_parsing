"""Multiple Of condition module."""
from typing import ClassVar
from parsing_assignment.conditions.base import BaseCondition


class MultipleOfCondition(BaseCondition):
    """Multiple of condition class.

    Checks if the line index is a multiple of a specific integer.
    If yes, format the line with this information embedded.

    """

    _prefix: ClassVar[str] = "Multiple de"

    def __init__(self, integer: int = 5) -> None:
        """Constructs a MultipleOfCondition object.

        Args:
            integer: Integer to check.

        """
        self._integer = integer

    def _is_satisfied(self, line_index: int, _: str) -> bool:
        """Checks if the line index is a multiple of a specific integer.

        Args:
            line_index: Line index.
            _: Line data.

        Returns:
            True if condition is satisfied, otherwise False

        """
        return line_index % self._integer == 0

    def _format_line(self, _: int, __: str) -> str:
        """Embeds the line with the line index information.

        Args:
            _: Line index.
            __: Line data.

        Returns:
            Formatted line data.

        """
        return f"{self._prefix} {self._integer}"
