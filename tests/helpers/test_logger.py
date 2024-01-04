import logging
import pytest
from parsing_assignment.helpers.logger import logger


def test_given_line_when_logging_it_then_success(caplog: pytest.LogCaptureFixture) -> None:
    logger.addHandler(caplog.handler)
    with caplog.at_level(logging.INFO):
        logger.output(56, "line data.")

    assert caplog.messages[-1] == "56 : line data."
    assert "56 : line data." in caplog.text
