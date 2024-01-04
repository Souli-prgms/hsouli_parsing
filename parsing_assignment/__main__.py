"""Main function."""
from fire import Fire  # type: ignore[import-untyped]
from parsing_assignment.parser import parse_log_file

if __name__ == "__main__":
    Fire(parse_log_file)
