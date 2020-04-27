import pytest
from Bank.account import Account
from faker import Faker


acc = None
def setup_function(function):
    global acc
    Faker.seed(0)
    acc = Account("John", "Doe")
    return acc

# @pytest.fixture(scope='')
# def acc():
#     Faker.seed(0)
#     acc = Account("John", "Doe")
#     return acc
#
# testy zawsze od test_


def test_basic():
    acc_number = str(acc)
    assert acc_number == 'GB22VTKG87647593824219'


def test_basic_2():
    Faker.seed(1)
    acc_number = str(Account("John", "Doe"))
    assert acc_number == 'GB42DWTG77763170669074'


def test_owner_name():
    # when
    owner_name = acc.owner()

    # then
    assert owner_name == "John Doe"


def test_balance():
    # when
    balance = acc.get_balance()

    # then
    assert balance == 0


def test_transfer():
    # when
    acc.transfer(-100)
    balance = acc.get_balance()

    # then
    assert balance == -100


def test_transfer1():
    # when
    acc.transfer(-100)
    acc.transfer(100)
    balance = acc.get_balance()

    # then
    assert balance == 0

def test_transfer2():
    # when
    acc.transfer(-100)
    acc.transfer(50)
    balance = acc.get_balance()

    # then
    assert balance == -50
