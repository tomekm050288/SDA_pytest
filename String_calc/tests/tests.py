import pytest
from string_calc_pack.string_calc import StringCalculator


@pytest.fixture(scope='module')
def calc():
    calc = StringCalculator()
    return calc

def test_add(calc):
    #given
    result = calc.add("")

    #when
    exp_result = 0

    #then

    assert result == exp_result


def test_add1(calc):
    #given
    result = calc.add("1,2,3,-1")

    #when
    exp_result = "negatives not allowed: -1"

    #then

    assert result == exp_result


def test_add2(calc):
    #given
    result = calc.add("1,2,3,1")

    #when
    exp_result = 7

    #then

    assert result == exp_result


def test_add3(calc):
    #given
    result = calc.add("1\n2,3,0")

    #when
    exp_result = 6

    #then

    assert result == exp_result

def test_add4(calc):
    #given
    result = calc.add("\naaaa")

    #when
    exp_result = "Wrong input"

    #then

    assert result == exp_result

def test_add5(calc):
    #given
    result = calc.add("\naaaa1")

    #when
    exp_result = "Wrong input"

    #then

    assert result == exp_result

def test_add6(calc):
    #given
    result = calc.add("5")

    #when
    exp_result = 5
    #then

    assert result == exp_result

def test_add7(calc):
    #given
    result = calc.add("a,1,6\n2")

    #when
    exp_result = "Wrong input"
    #then

    assert result == exp_result

def test_add8(calc):
    # given
    result = calc.add("0,1,6\n2,1000,1001")

    # when
    exp_result = 1009
    # then

    assert result == exp_result

def test_add9(calc):
    # given
    result = calc.add("0,1,6\n2,1000p1001")

    # when
    exp_result = "Wrong input"
    # then

    assert result == exp_result


def test_add10(calc):
    # given
    result = calc.add("//abc\n5,3\n0abcdf5,5,0,01")

    # when
    exp_result = "Wrong input"
    # then

    assert result == exp_result

def test_add11(calc):
    # given
    result = calc.add("//abc-1,5\n8,-6")

    # when
    exp_result = "negatives not allowed: -1, -6"
    # then

    assert result== exp_result

def test_add12(calc):
    # given
    result = calc.add("//abc\n5,3\n0abc5,5,0,1")

    # when
    exp_result = 19
    # then

    assert result == exp_result



















# def test_add9(self):
#     # given
#     result = self.string_calc.add("10,20,20")
#
#     # when
#     exp_result = 50
#     # then
#
#     self.assertEqual(result, exp_result)
#
# def test_add10(self):
#     # given
#     result = self.string_calc.add("//###10,20###20")
#
#     # when
#     exp_result = 50
#     # then
#
#     self.assertEqual(result, exp_result)
#
# def test_add11(self):
#     # given
#     result = self.string_calc.add("\n1\n1,4,")
#
#     # when
#     exp_result = "Wrong input"
#     # then
#
#     self.assertEqual(result, exp_result)
#
# "//abc\n5,3\n0abc5,5,0,-1\n"
#

#

#
# def test_add15(self):
#     # given
#     result = self.string_calc.add("1\n6\n8,-6,-8,-9")
#
#     # when
#     exp_result = "negatives not allowed: -6, -8, -9"
#     # then
#
#     self.assertEqual(result, exp_result)
#




