from to_test import sum_all
import pytest


@pytest.mark.parametrize("test_input, expected", [
    ((1, 2, 3), 6),
    ((1.0, 2, -3), 0),
])
def test_sum_all_possitive(test_input, expected):
    assert sum_all(*test_input) == expected


def test_sum_all_none():
    with pytest.raises(TypeError) as e_info:
        sum_all(None)


def test_sum_all_str():
    with pytest.raises(TypeError) as e_info:
        sum_all("str")


def test_sum_all_generator():
    assert sum_all(*range(5)) == 10






