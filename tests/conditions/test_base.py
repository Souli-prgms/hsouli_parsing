import pytest
from parsing_assignment.conditions.base import BaseCondition, ChainOfConditions


class DummyCondition(BaseCondition):
    def __init__(self, diff: int = 0) -> None:
        self.diff = diff

    def _is_satisfied(self, line_index: int, __: str) -> bool:
        return line_index == self.diff

    def _format_line(self, _: int, __: str) -> str:
        return str(self.diff)


class ErrorCondition(BaseCondition):
    def _is_satisfied(self, line_index: int, __: str) -> bool:
        raise RuntimeError()

    def _format_line(self, _: int, __: str) -> str:
        raise RuntimeError()


def test_given_condition_when_handling_line_then_success():
    condition = DummyCondition(1)
    assert condition._is_satisfied(1, "")
    assert not condition._is_satisfied(0, "")
    assert condition.handle(1, "") is not None
    assert condition.handle(0, "") is None


def test_given_two_conditions_when_adding_them_then_creates_valid_chain() -> None:
    chain = DummyCondition(-1) + DummyCondition(1)
    assert isinstance(chain, ChainOfConditions)
    assert len(chain.conditions) == 2
    assert chain.conditions[0].diff == -1
    assert chain.conditions[1].diff == 1


def test_given_wrong_type_when_adding_condition_then_raises_error() -> None:
    with pytest.raises(NotImplementedError):
        DummyCondition(1) + "test"


def test_given_chain_when_adding_condition_then_success():
    chain = ChainOfConditions([])
    chain += DummyCondition(1)
    assert len(chain.conditions) == 1
    assert (
        len((DummyCondition(1) + DummyCondition(1) + DummyCondition(1)).conditions) == 3
    )


def test_given_chain_when_processing_line_then_success() -> None:
    chain = DummyCondition(0) + DummyCondition(-1) + DummyCondition(5)

    assert chain.handle(0, "") == "0"
    assert chain.handle(5, "") == "5"
    assert chain.handle(2, "") == ChainOfConditions._default_return


def test_given_critical_condition_when_chaining_conditions_then_ignores_it() -> None:
    chain = ErrorCondition() + DummyCondition(0)
    assert chain.handle(0, "") == "0"
