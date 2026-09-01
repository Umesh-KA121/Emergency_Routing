from app.services.dsa.graph import Graph
from app.services.dsa.routing import RoutingEngine


def test_routing_engine_finds_shortest_route():
    graph = Graph()

    graph.add_edge("A", "B", 4)
    graph.add_edge("A", "C", 2)
    graph.add_edge("C", "B", 1)
    graph.add_edge("B", "D", 5)
    graph.add_edge("C", "D", 8)

    routing_engine = RoutingEngine(graph)

    result = routing_engine.find_shortest_route("A", "D")

    assert result["distance"] == 8
    assert result["path"] == ["A", "C", "B", "D"]


def test_routing_engine_handles_unreachable_destination():
    graph = Graph()

    graph.add_node("A")
    graph.add_node("B")

    routing_engine = RoutingEngine(graph)

    result = routing_engine.find_shortest_route("A", "B")

    assert result["distance"] == float("inf")
    assert result["path"] == []


def test_routing_engine_same_location():
    graph = Graph()

    graph.add_node("A")

    routing_engine = RoutingEngine(graph)

    result = routing_engine.find_shortest_route("A", "A")

    assert result["distance"] == 0
    assert result["path"] == ["A"]