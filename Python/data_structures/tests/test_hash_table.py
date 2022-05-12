from data_structures.hash_table import HashTable, Node
import pytest


@pytest.fixture
def ht_example() -> HashTable:
    """Hash table fixture"""
    ht_example = HashTable(30, 16)
    for i in range(4):
        ht_example.insert(i, str(i))
    return ht_example


@pytest.fixture
def ht_empty_example():
    """Empty hash table fixture"""
    ht_example = HashTable(30, 16)
    return ht_example


def test_ht_init(ht_empty_example):
    """Test hash table init method"""
    assert ht_empty_example.get__hash_str() == " " * 16 * 30


@pytest.mark.parametrize("item", [4, 5, 6])
def test_lookup(ht_empty_example, item):
    """Test lookup method"""
    ht_empty_example.insert(item, item)
    assert ht_empty_example.lookup(item) == item


@pytest.mark.parametrize("items", [[1, 2], ["q", "w", "e"]])
def test_insert(ht_empty_example, items):
    """Test insert method"""
    for item in items:
        ht_empty_example.insert(item, item)
        assert ht_empty_example.lookup(item) == item


@pytest.mark.parametrize("items", [[1, 2, "q", "w", "e"]])
def test_insert_type_error(ht_empty_example, items):
    """Test insert method"""
    with pytest.raises(TypeError):
        for item in items:
            ht_empty_example.insert([], str(item))


@pytest.mark.parametrize("item", [4, 5, 6])
def test_lookup_key_error(ht_example, item):
    """Test lookup method key error"""
    with pytest.raises(ValueError):
        assert ht_example.lookup(item) is None


def test_delete(ht_example):
    """Test delete method"""
    ht_example.delete(2)
    with pytest.raises(ValueError):
        assert ht_example.lookup(2)