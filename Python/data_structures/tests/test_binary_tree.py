from data_structures.binary_tree import BinaryTree, Node
import pytest


@pytest.fixture
def bs_example() -> BinaryTree:
    """BinaryTree fixture"""
    bs_example = BinaryTree()
    for i in range(4):
        bs_example.insert(i)
    return bs_example


@pytest.fixture
def bs_empty_example():
    """Empty BinaryTree fixture"""
    bs_example = BinaryTree()
    return bs_example


def test_bst_init(bs_empty_example):
    """Test BS init method"""
    assert bs_empty_example.root is None


@pytest.mark.parametrize("items", [[1, 2], ["a", "b", "c"]])
def test_insert(bs_empty_example, items):
    """Test insert method"""
    for item in items:
        bs_empty_example.insert(item)
        assert bs_empty_example.lookup(item).data == item


@pytest.mark.parametrize("items", [[1, 2, "a", "b", "c"]])
def test_insert_type_error(bs_empty_example, items):
    """Test insert method"""
    with pytest.raises(TypeError):
        for item in items:
            bs_empty_example.insert(item)


@pytest.mark.parametrize("item", [4, 5, 6])
def test_lookup(bs_example, item):
    """Test lookup method"""
    bs_example.insert(item)
    assert bs_example.lookup(item).data == item


@pytest.mark.parametrize("item", [4, 5, 6])
def test_lookup_value_error(bs_example, item):
    """Test lookup method value error"""
    with pytest.raises(AttributeError):
        assert bs_example.lookup(item) is None


def test_delete(bs_example):
    """Test delete method"""
    with pytest.raises(AttributeError):
        bs_example.delete(2)
        assert bs_example.lookup(2) is None