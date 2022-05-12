from data_structures.stack import Stack
import pytest


@pytest.fixture
def stack_example() -> Stack:
    """Empty stack fixture"""
    stack = Stack()
    for i in range(4):
        stack.push(i)
    return stack


@pytest.fixture
def stack_empty_example() -> Stack:
    """Stack fixture"""
    stack = Stack()
    return stack


@pytest.mark.parametrize("test_input, expected", [('qwerty', 0), ((1, 2, "c", "d"), 0), ('bombom', 0)])
def test_push(stack_empty_example, test_input, expected):
    """Test push method"""
    stack_empty_example.push(test_input)
    assert stack_empty_example.lookup(test_input) == expected


def test_peek(stack_example):
    """Test peek method"""
    item = stack_example.peek()
    assert item == 3


def test_pop(stack_example):
    """Test pop method"""
    stack_example.pop()
    assert stack_example.peek() == 2
