from data_structures.linked_list import LinkedList
import pytest


@pytest.fixture
def list_empty_example() -> LinkedList:
    """Empty list fixture"""
    list_example = LinkedList()
    return list_example


@pytest.fixture
def list_example() -> LinkedList:
    """List fixture"""
    list_example = LinkedList()
    for i in range(4):
        list_example.append(i)
    return list_example


def test_list_init(list_empty_example):
    """Test list init method"""
    assert list_empty_example.head is None


@pytest.mark.parametrize("test_input, expected", [('qwerty', 0), ((1, 2, "c", "d"), 1), ('bombom', 2)])
def test_lookup(list_empty_example, test_input, expected):
        list_empty_example.append(test_input)
        assert list_empty_example.lookup(test_input) == expected


@pytest.mark.parametrize("test_input, expected", [('q', 0), ((1, 2, "c", "d"), 0), ('bombom', 0)])
def test_prepend(list_empty_example, test_input, expected):
        list_empty_example.prepend(test_input)
        assert list_empty_example.lookup(test_input) == expected


@pytest.mark.parametrize("test_input, index, expected", [('q', 1, 0), ((1, 2, "c", "d"), 5, 0), ('bombom', 3, 0)])
def test_insert(list_empty_example, test_input, index, expected):
    """Test clear method"""
    list_empty_example.insert(test_input, index)
    assert list_empty_example.lookup(test_input) == expected


@pytest.mark.parametrize("test_input, index, expected", [('q', 1, 1), ((1, 2, "c", "d"), 3, 3), ('bombom', 2, 2)])
def test_insert_filled(list_example, test_input, index, expected):
    """Test clear method"""
    list_example.insert(test_input, index)
    assert list_example.lookup(test_input) == expected


def test_delete(list_example):
    """Test delete method"""
    assert list_example.lookup(2) == 2
    list_example.delete(2)
    assert list_example.lookup(2) is None

