"""Parser module."""
# from parsing_assignment.helpers.timer import timer
from parsing_assignment.helpers.io import open_file
from parsing_assignment.helpers.logger import logger
from parsing_assignment.conditions import (
    MultipleOfCondition,
    JsonCondition,
    CharExistenceCondition,
    SuffixCondition,
)


# @timer
def parse_log_file(filepath: str) -> None:
    """Parses specific log file.

    Args:
        filepath: Local log file path.

    """
    chain = (
        MultipleOfCondition()
        + CharExistenceCondition()
        + SuffixCondition()
        + JsonCondition()
    )

    for line_index, line_content in open_file(filepath):
        # for better performances, we could decouple the chain processing and the logging
        # in order to process lines in parallel (for big log files)
        # we could also have used cython for optimization

        new_data = chain.handle(line_index, line_content)
        logger.output(line_index, new_data)
