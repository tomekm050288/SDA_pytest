import pytest
from Queue.queue import queue_time


def test_queue_basic():
    result = queue_time([10], 4)
    assert result == 10


def test_queue_basic2():
    result = queue_time([], 4)
    assert result == 0


def test_queue1():
    result = queue_time([10, 2, 3, 3], 2)
    assert result == 10


def test_queue2():
    result = queue_time([5, 3, 4], 1)
    assert result == 12


def test_queue3():
    result = queue_time([2, 3, 10], 2)
    assert result == 12


def test_queue4():
    result = queue_time([0, 0, 0], 7)
    assert result == 0
