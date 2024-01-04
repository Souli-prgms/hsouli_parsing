from parsing_assignment.conditions import SuffixCondition

condition = SuffixCondition()


def test_given_suffix_condition_when_processing_it_then_success() -> None:
    assert condition.handle(1, " {}") is None
    assert (
        condition.handle(0, "Process 498758 succesfully run.")
        == "Process 498758 succesfully run."
    )
