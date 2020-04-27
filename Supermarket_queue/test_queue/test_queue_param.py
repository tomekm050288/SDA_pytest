from Queue.queue import queue_time
import pytest


@pytest.mark.parametrize('customers, n, result',
                         [([10, 2, 3, 3], 2, 10),
                          ([10, 2, 3, 3], 2, 10),
                          ([2, 3, 10], 2, 12),
                          ([5, 3, 4], 1, 12),
                          ([0, 0, 0], 7, 0)
                          ]
                         )
def test_queue_basic(customers, n, result):
    assert result == queue_time(customers, n)
