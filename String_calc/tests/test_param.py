import pytest
from string_calc_pack.string_calc import StringCalculator

@pytest.mark.parametrize('value, result,',
                         [("1,2,3,-1","negatives not allowed: -1")
                          ]
                         )


def test_add(value, result):
    calc = StringCalculator()
    assert result == calc.add(value)
