from app.services.dsa.graph import Graph


def test_graph_creation():
    graph = Graph()

    graph.add_edge("A", "B", 5)
    graph.add_edge("A", "C", 3)

    assert "A" in graph.get_nodes()
    assert "B" in graph.get_nodes()
    assert "C" in graph.get_nodes()

    assert ("B", 5) in graph.get_neighbors("A")
    assert ("C", 3) in graph.get_neighbors("A")