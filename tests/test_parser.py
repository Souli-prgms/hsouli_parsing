import logging
import pytest
import re
from parsing_assignment.parser import parse_log_file
from parsing_assignment.helpers.logger import logger
from tests import EXAMPLE_PATH


def test_given_log_file_when_parsing_it_then_success(
    caplog: pytest.LogCaptureFixture,
) -> None:
    logger.addHandler(caplog.handler)
    with caplog.at_level(logging.INFO):
        parse_log_file(EXAMPLE_PATH)

    assert len(caplog.messages) == 17
    for index, message in enumerate(caplog.messages):
        match = re.match(f"^{index} : (.*?)$", message)
        assert match is not None
