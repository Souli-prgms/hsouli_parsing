"""Suffix condition module."""
import re
from parsing_assignment.conditions.base import BaseCondition


class SuffixCondition(BaseCondition):
    """Suffix condition class.

    Checks if the line ends with a specific suffix.
    If yes, returns the line as it is.

    """

    def __init__(self, suffix: str = ".") -> None:
        """Constructs a SuffixCondition object.

        Args:
            suffix: Suffix to check (string, so we can check multiple characters).

        """
        self._suffix = suffix

    def _is_satisfied(self, _: int, line_content: str) -> bool:
        """Checks if the line ends with a specific suffix.

        Args:
            _: Line index.
            line_content: Line data.

        Returns:
            True if condition is satisfied, otherwise False

        """
        clean_string = re.sub(r"\\n|\\r", "", line_content)
        return clean_string.endswith(self._suffix)

    def _format_line(self, _: int, line_content: str) -> str:
        """Leave the line content as it is.

        Args:
            _: Line index.
            line_content: Line data.

        Returns:
            Line data.

        """
        return line_content
