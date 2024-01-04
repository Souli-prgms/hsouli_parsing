"""Base condition module."""
from __future__ import annotations
from typing import ClassVar
from abc import ABC, abstractmethod


class BaseCondition(ABC):
    """Base condition class."""

    @abstractmethod
    def _is_satisfied(self, line_index: int, line_content: str) -> bool:
        pass

    @abstractmethod
    def _format_line(self, line_index: int, line_content: str) -> str:
        pass

    def handle(self, line_index: int, line_content: str) -> str | None:
        """Processes line.
        If specific condition matches, format the line and return it.
        Otherwise, return None.

        Args:
            line_index: Line index.
            line_content: Line data.

        Returns:
            Formatted line if condition matches, otherwise None.

        """
        if self._is_satisfied(line_index, line_content):
            return self._format_line(line_index, line_content)

        return None

    def __add__(self, other: BaseCondition) -> ChainOfConditions:
        """Chains conditions together.

        Args:
            other: Other condition.

        Returns:
            Chain containing both conditions together.

        Raises:
            NotImplementedError: If other is not a BaseCondition

        """
        if not isinstance(other, BaseCondition):
            raise NotImplementedError()

        return ChainOfConditions([self, other])


class ChainOfConditions:
    """
    Chain of conditions.

    Used to pass lines to conditions in a sequential order.
    Implemented so we can dynamically group conditions together.
    """

    _default_return: ClassVar[str] = "Rien à afficher"

    def __init__(self, conditions: list[BaseCondition]) -> None:
        """
        Constructs a chain of conditions.

        Args:
            conditions: Conditions to chain.

        """
        self.conditions = conditions

    def __add__(self, other: BaseCondition) -> ChainOfConditions:
        """Adds a new condition to the chain.

        Args:
            other: Other condition to add

        Returns:
            Current chain of conditions, with other condition added at the end

        Raises:
            NotImplementedError: If other is not a BaseCondition

        """
        if not isinstance(other, BaseCondition):
            raise NotImplementedError()

        self.conditions.append(other)
        return self

    def handle(self, line_index: int, line_content: str) -> str:
        """
        Processes a specific line.

        Args:
            line_index: Line index.
            line_content: Line data.

        Returns:
            Formatted line data.

        """
        for condition in self.conditions:
            try:
                condition_value = condition.handle(line_index, line_content)
                if condition_value is not None:
                    return condition_value
            except:  # pylint: disable=bare-except
                continue

        return self._default_return
