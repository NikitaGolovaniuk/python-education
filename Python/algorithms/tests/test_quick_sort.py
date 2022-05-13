from algorithms.quick_sort import quick_sort
from random import randint
import pytest

@pytest.mark.parametrize("test_input", [[randint(-1000, 1000) for i in range(1000)] for j in range(1000)])
def test_quick_sort(test_input):
    assert sorted(test_input) == quick_sort(test_input)


def test_type_error():
    arr = ['q', 2, 'e']
    with pytest.raises(TypeError):
        assert quick_sort(arr) == sorted(arr)