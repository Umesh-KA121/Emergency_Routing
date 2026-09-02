import pytest

from app.services.dsa.a_star import a_star, heuristic
from app.services.dsa.graph import Graph


def create_test_graph():
    graph = Graph()

    graph.add_node("A", 0, 0)
    graph.add_node("B", 2, 0)
    graph.add_node("C", 0, 2)
    graph.add_node("D", 2, 2)

    graph.add_edge("A", "B", 2)
    graph.add_edge("A", "C", 2)
    graph.add_edge("B", "D", 2)
    graph.add_edge("C", "D", 2)

    return graph


def test_heuristic():
    graph = create_test_graph()

    assert heuristic(graph, "A", "D") == pytest.approx(
        2.828427,
        rel=1e-5,
    )


def test_a_star_shortest_path():
    graph = create_test_graph()

    distance, path = a_star(graph, "A", "D")

    assert distance == 4
    assert path in [
        ["A", "B", "D"],
        ["A", "C", "D"],
    ]


def test_a_star_same_source_destination():
    graph = create_test_graph()

    distance, path = a_star(graph, "A", "A")

    assert distance == 0
    assert path == ["A"]


def test_a_star_unreachable_destination():
    graph = Graph()

    graph.add_node("A", 0, 0)
    graph.add_node("B", 5, 5)

    distance, path = a_star(graph, "A", "B")

    assert distance == float("inf")
    assert path == []


def test_a_star_invalid_start():
    graph = create_test_graph()

    with pytest.raises(ValueError):
        a_star(graph, "X", "A")


def test_a_star_invalid_destination():
    graph = create_test_graph()

    with pytest.raises(ValueError):
        a_star(graph, "A", "X")


def test_a_star_requires_coordinates():
    graph = Graph()

    graph.add_node("A")
    graph.add_node("B")

    graph.add_edge("A", "B", 5)

    with pytest.raises(ValueError):
        a_star(graph, "A", "B")