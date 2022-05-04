from to_test import even_odd
import pytest


@pytest.mark.parametrize("test_input, expected", [(2, "even"), (1, "odd"),
                                                  (-2, "even"), (-1, "odd"),
                                                  (12.0, "even"), (-123, "odd")])
def test_even_odd_num(test_input, expected):
    assert even_odd(test_input) == expected


def test_even_odd_val():
    with pytest.raises(TypeError) as e_info:
        even_odd("str")


