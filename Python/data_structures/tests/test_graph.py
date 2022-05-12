from data_structures.graph import Graph, Node
import pytest

A, B, C, D = Node('q'), Node('w'), Node('e'), Node(1)


@pytest.fixture
def graph_example() -> Graph:
    """Graph fixture"""
    graph_example = Graph()
    graph_example.insert(A)
    graph_example.insert(B, A)
    graph_example.insert(C, A, B)
    return graph_example


@pytest.fixture
def graph_empty_example():
    """Empty graph fixture"""
    graph_example = Graph()
    return graph_example


@pytest.mark.parametrize("items", [[A], [B, A], [C, A, B]])
def test_insert(graph_empty_example, items):
    """Test insert method"""
    for item in items:
        graph_empty_example.insert(item)
        assert graph_empty_example.lookup(item.data).data == item.data


@pytest.mark.parametrize("item", [A, B, C])
def test_lookup(graph_example, item):
    """Test lookup method"""
    assert graph_example.lookup(item.data) == item


@pytest.mark.parametrize("item", [D])
def test_lookup_value_error(graph_example, item):
    """Test lookup method"""
    with pytest.raises(ValueError):
        graph_example.lookup(item)


def test_delete(graph_example):
    """Test delete method"""
    assert graph_example.lookup(B.data) == B
    graph_example.delete(B)
    with pytest.raises(ValueError):
        assert graph_example.lookup(B.data) == B
