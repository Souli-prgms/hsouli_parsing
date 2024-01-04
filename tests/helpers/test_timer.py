import pytest
import re
from parsing_assignment.helpers.timer import timer


@timer
def add(a: int, b: int) -> int:
    return a + b


def test_given_function_when_timing_it_then_success(capfd: pytest.CaptureFixture) -> None:
    add(1, 1)
    out, err = capfd.readouterr()
    match = re.match(r"^\d+\.\d+ seconds elapsed$", out)
    assert match is not None
    assert err == ""
