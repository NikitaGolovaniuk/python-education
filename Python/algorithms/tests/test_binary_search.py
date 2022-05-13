from algorithms.binary_search import binary_search
from random import randint
import pytest


@pytest.mark.parametrize("test_input", [[randint(-1000, 1000) for i in range(1000)] for i in range(1000)])
def test_binary_search(test_input):
    test_input.sort()
    value = randint(0, 999)
    if binary_search(test_input, value):
        assert test_input[binary_search(test_input, value)] == value


def test_binary_search_assertion_error():
    test_input = ['q', 'w', 'e', 'r', 't', 'y']
    with pytest.raises(AssertionError):
        assert binary_search(test_input, 'w')