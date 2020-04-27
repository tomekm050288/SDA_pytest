import pytest
from Bank.account import Account
from Bank.card_server import Card
from faker import Faker
from unittest.mock import patch, MagicMock


@pytest.fixture(scope='module')
def patcher():
    patcher = patch('Bank.card_server.Server.validate_card', return_value=True)
    return patcher


@pytest.fixture(scope='function')
def acc():
    Faker.seed(0)
    acc = Account("John", "Doe")
    return acc


def test1(patcher, acc):
    card = Card(acc, 345)
    assert card.is_pin_number()



@patch('Bank.card_server.Server.validate_card')
def test(def_conn_mock, acc):
    conn_mock = MagicMock(return_value=True)
    def_conn_mock.return_value = conn_mock
    card = Card(acc, 345)
    assert card.is_pin_number()
#
#
# @patch('Bank.card_server.Server.validate_card')
# def test2(def_conn_mock, acc):
#     conn_mock = MagicMock(return_value=True)
#     def_conn_mock.return_value = conn_mock
#     card = Card(acc, 125)
#     assert card.is_pin_number()
#
# @patch('Bank.card_server.Server.validate_card')
# def test3(def_conn_mock, acc):
#     conn_mock = MagicMock(return_value=True)
#     def_conn_mock.return_value = conn_mock
#     card = Card(acc, 'aaa')
#     assert card.is_pin_number() == "Validation error"
#
#
# def test_get_account(acc):
#     # given
#     pin = '1235'
#     card = acc.create_card("1235")
#
#     # when
#     number = card.get_account()
#
#     # then
#     assert number == acc.acc_number

