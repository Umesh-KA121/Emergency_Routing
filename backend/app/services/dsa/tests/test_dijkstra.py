from app.services.dsa.graph import Graph
from app.services.dsa.dijkstra import dijkstra


def test_dijkstra_shortest_path():
    graph = Graph()

    graph.add_edge("A", "B", 4)
    graph.add_edge("A", "C", 2)
    graph.add_edge("C", "B", 1)
    graph.add_edge("B", "D", 5)
    graph.add_edge("C", "D", 8)

    distance, path = dijkstra(graph, "A", "D")

    assert distance == 8
    assert path == ["A", "C", "B", "D"]


def test_dijkstra_same_source_destination():
    graph = Graph()

    graph.add_node("A")

    distance, path = dijkstra(graph, "A", "A")

    assert distance == 0
    assert path == ["A"]


def test_dijkstra_unreachable_destination():
    graph = Graph()

    graph.add_node("A")
    graph.add_node("B")

    distance, path = dijkstra(graph, "A", "B")

    assert distance == float("inf")
    assert path == []


def test_dijkstra_invalid_start():
    graph = Graph()

    graph.add_node("A")

    try:
        dijkstra(graph, "X", "A")
        assert False
    except ValueError:
        assert True


def test_dijkstra_invalid_destination():
    graph = Graph()

    graph.add_node("A")

    try:
        dijkstra(graph, "A", "X")
        assert False
    except ValueError:
        assert True