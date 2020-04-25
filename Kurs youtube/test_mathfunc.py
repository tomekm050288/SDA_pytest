from math_func import add
import pytest
import sys


#@pytest.mark.skipif(reason="do not run number add test")
@pytest.mark.skipif(sys.version_info < (3, 3), reason="do not run number add test")
def test_add_int():
    assert add(7, 3) == 10
    assert add(10) == 12
    print(add(7, 3), "--------------------------------------------")


def test_add_int2():
    assert add(7, 5) == 12
    assert add(10) == 12
    assert add(0) == 2
    assert add(5, 10) < 20


def test_add_string():
    result = add('Hello', ' World')
    assert result == 'Hello World'
    assert type(result) is str
    assert 'dfd' not in result


def test_add_float():
    result = add(1.8, 1.9)
    assert result == 3.7
