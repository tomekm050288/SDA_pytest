from math_func import add
import pytest


@pytest.mark.parametrize('num1, num2, result',
                         [(7, 3, 10),
                          ('Hello', " World", "Hello World"),
                          (1.8, 1.9, 3.7)
                          ]
                         )

def test_add(num1, num2, result):
    assert add(num1, num2) == result
