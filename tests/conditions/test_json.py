from parsing_assignment.conditions import JsonCondition

condition = JsonCondition()


def test_given_char_json_condition_when_processing_it_then_success() -> None:
    assert condition.handle(1, " {}") is None
    assert condition.handle(0, '{"test": true}') == '{"test":true,"pair":true}'
    assert condition.handle(1, '{"test": true}') == '{"test":true,"pair":false}'
