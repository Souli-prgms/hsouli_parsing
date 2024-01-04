from parsing_assignment.conditions import MultipleOfCondition

condition = MultipleOfCondition()


def test_given_multiple_of_condition_when_processing_it_then_success() -> None:
    assert condition.handle(1, " {}") is None
    assert condition.handle(0, '{"test": true}') == "Multiple de 5"
    assert condition.handle(675, '{"test": true}') == "Multiple de 5"
