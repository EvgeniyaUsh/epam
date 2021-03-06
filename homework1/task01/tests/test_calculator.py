import pytest
from task01.calculator.calc import check_power_of_2


# test for calculator/calc.py
@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (65536, True),
        (12, False),
        (0, False),
        (1, True),
        (-22, False),
        (16, True),
    ],
)
def test_power_of_2(value: int, expected_result: bool):
    actual_result = check_power_of_2(value)

    assert actual_result == expected_result
