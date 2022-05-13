from algorithms.recursive_factorial import factorial
from math import factorial
import pytest


@pytest.mark.parametrize("test_input", [val for val in range(100)])
def test_factorial(test_input):
    assert factorial(test_input) == factorial(test_input)


def test_factorial_errors():
    with pytest.raises(TypeError):
        assert factorial("qwerty")
    with pytest.raises(ValueError):
        assert factorial(-1)
