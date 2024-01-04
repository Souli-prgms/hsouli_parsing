"""Char existence condition module."""
from parsing_assignment.conditions.base import BaseCondition


class CharExistenceCondition(BaseCondition):
    """Char existence condition class.

    Checks if a specific character exists in line.
    If yes, it replaces a specific character with another character.

    """

    def __init__(
        self, chars: str = "$", old_value: str = " ", new_value: str = "_"
    ) -> None:
        """Constructs a CharExistenceCondition object

        Args:
            chars: Chars to check (string, so we can have multiple characters)
            old_value: Old value to replace by.
            new_value: New value to replace with.

        """
        self._chars = chars
        self._new = new_value
        self._old = old_value

    def _is_satisfied(self, _: int, line_content: str) -> bool:
        """Checks if line contains specific characters.

        Args:
            _: Line index.
            line_content: Line data.

        Returns:
            True if condition is satisfied, otherwise False

        """
        return self._chars in line_content

    def _format_line(self, _: int, line_content: str) -> str:
        """Replace old value in line with new value.

        Args:
            _: Line index.
            line_content: Line data.

        Returns:
            Formatted line data.

        """
        return line_content.replace(self._old, self._new)
