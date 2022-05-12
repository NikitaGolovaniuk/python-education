from data_structures.queue import Queue
import pytest


@pytest.fixture
def queue_example() -> Queue:
    """Empty queue fixture"""
    queue_example = Queue()
    for i in range(4):
        queue_example.enqueue(i)
    return queue_example


@pytest.fixture
def queue_empty_example() -> Queue:
    """Queue fixture"""
    queue_example = Queue()
    return queue_example


@pytest.mark.parametrize("test_input, expected", [('qwerty', 0), ((1, 2, "c", "d"), 0), ('bombom', 0)])
def test_enqueue(queue_empty_example, test_input, expected):
    """Test enqueue method"""
    queue_empty_example.enqueue(test_input)
    assert queue_empty_example.lookup(test_input) == expected


def test_dequeue(queue_example):
    """Test dequeue method"""
    item = queue_example.dequeue()
    assert item == 3


def test_peek(queue_example):
    """Test peek method"""
    item = queue_example.peek()
    assert item == 3
