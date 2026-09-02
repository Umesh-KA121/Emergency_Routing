import pytest

from app.services.dsa.graph import Graph


def test_graph_creation():
    graph = Graph()

    graph.add_edge("A", "B", 5)
    graph.add_edge("A", "C", 3)

    assert "A" in graph.get_nodes()
    assert "B" in graph.get_nodes()
    assert "C" in graph.get_nodes()


def test_bidirectional_edge():
    graph = Graph()

    graph.add_edge("A", "B", 5)

    assert ("B", 5) in graph.get_neighbors("A")
    assert ("A", 5) in graph.get_neighbors("B")


def test_one_way_edge():
    graph = Graph()

    graph.add_edge("A", "B", 5, bidirectional=False)

    assert ("B", 5) in graph.get_neighbors("A")
    assert ("A", 5) not in graph.get_neighbors("B")


def test_negative_weight_rejected():
    graph = Graph()

    with pytest.raises(ValueError):
        graph.add_edge("A", "B", -5)

def test_node_coordinates():
    graph = Graph()

    graph.add_node("A", 31.6340, 74.8723)

    assert graph.get_coordinates("A") == (31.6340, 74.8723)