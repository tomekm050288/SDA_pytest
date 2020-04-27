import pytest
from Bank.account import Account
from faker import Faker

DEBUG = False


@pytest.fixture(scope='module')
def acc():
    Faker.seed(0)
    acc = Account("John", "Doe")
    return acc


def test_basic(acc):
    # given
    card = acc.create_card("4567")

    # when
    owner = card.card_owner

    #then
    assert owner == acc.owner()

def test_check_pin(acc):
    # given
    pin = '1235'
    card = acc.create_card("1235")

    # when
    is_pin_ok = card.check_pin(pin)

    #then
    assert is_pin_ok is True


def test_get_account(acc):
    # given
    pin = '1235'
    card = acc.create_card("1235")

    # when
    number = card.get_account()

    # then
    assert number == acc.acc_number


def test_ispin_number(acc):
    # given
    pin = 'aaa1235'
    card = acc.create_card("1235")

    # when
    is_pin_ok = card.check_pin(pin)

    #then
    assert is_pin_ok is False
