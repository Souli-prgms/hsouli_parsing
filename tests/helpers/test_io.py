import pytest
from parsing_assignment.helpers.io import open_file
from tests import EXAMPLE_PATH


def test_given_existing_log_file_when_reading_it_then_success() -> None:
    lines = list(open_file(EXAMPLE_PATH))

    assert len(lines) == 17
    for expected_index, (index, _) in enumerate(lines):
        assert index == expected_index


def test_given_non_existing_log_file_when_reading_it_then_fails() -> None:
    with pytest.raises(RuntimeError):
        list(open_file("dummy_file.txt"))
