from project.example import *
from unittest import mock
import unittest

def test_print_contest_of_cwd_():
    actual_result = print_contest_if_cwd()

    expected_dir = b'test_project.py'
    assert expected_dir in actual_result

# użycie dekoratora mock.patch
@mock.patch('project.example.check_output', return_value=b'foo\nbar\n')
def test_print_contest_of_cwd(mock_check_output):
    actual_result = print_contest_if_cwd()

    expected_dir = b'foo'
    assert expected_dir in actual_result

# można tak udekorowac klasę
@mock.patch('project.example.check_output', return_value=b'foo\nbar\n')
class Test_Example(unittest.TestCase):

    def test_print_contest_of_cwd(self, mock_check_output):
        actual_result = print_contest_if_cwd()
        expected_dir = b'foo'
        self.assertIn(expected_dir, actual_result)


# przy uzyciu context managera
def test_print_contest_of_cwd2():
    with mock.patch('project.example.check_output', return_value=b'foo\nbar\n'):
        actual_result = print_contest_if_cwd()
    expected_dir = b'foo'
    assert expected_dir in actual_result


# stworzenie mocka w setup
class Test_Example2(unittest.TestCase):

    def setUp(self):
        self.patcher = mock.patch('project.example.check_output', return_value=b'1\n2345')
        self.patcher.start()

    def test_print_contest_of_cwd(self):
        actual_result = print_contest_if_cwd()
        expected_dir = b'1'
        self.assertIn(expected_dir, actual_result)

    def tearDown(self):
        self.patcher.stop()














