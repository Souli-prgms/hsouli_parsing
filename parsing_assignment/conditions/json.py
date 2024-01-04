"""Json condition module."""
import orjson  # Using orjson because it's faster
from parsing_assignment.conditions.base import BaseCondition


class JsonCondition(BaseCondition):
    """Json condition class.

    Checks if line starts with a left bracket.
    If yes, Serializes the line as a JSON dict.
    Also adds info regarding the parity of the line index.
    Finally, re-serializes the JSON dict.

    """

    def _is_satisfied(self, line_index: int, line_content: str) -> bool:
        """
        Checks if line starts with a left bracket.

        Args:
            line_index: Line index.
            line_content: Line data.

        Returns:
            True if condition is satisfied, otherwise False

        """
        return line_content.startswith("{")

    def _format_line(self, line_index: int, line_content: str) -> str:
        """Serializes the line as a JSON dict.
        Adds info regarding the parity of the line index and re-serializes the JSON dict.

        Args:
            line_index: Line index.
            line_content: Line data.

        Returns:
            Formatted line data.

        """
        data = orjson.loads(line_content)  # pylint: disable=no-member
        data["pair"] = line_index % 2 == 0
        return orjson.dumps(data).decode("utf-8")  # pylint: disable=no-member
