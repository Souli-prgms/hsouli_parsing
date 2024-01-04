from parsing_assignment.conditions import CharExistenceCondition

condition = CharExistenceCondition()


def test_given_char_existence_condition_when_processing_it_then_success() -> None:
    assert condition.handle(1, "test test") is None
    assert condition.handle(1, "test$ test") == "test$_test"
