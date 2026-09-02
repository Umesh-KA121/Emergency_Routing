import math

from app.services.dsa.graph import Graph
from app.services.dsa.priority_queue import PriorityQueue


def heuristic(graph: Graph, node, destination):
    """
    Calculate the Euclidean distance between two nodes.
    """

    node_coordinates = graph.get_coordinates(node)
    destination_coordinates = graph.get_coordinates(destination)

    if node_coordinates is None or destination_coordinates is None:
        raise ValueError(
            "Both nodes must have coordinates for A* search."
        )

    node_lat, node_lon = node_coordinates
    destination_lat, destination_lon = destination_coordinates

    return math.sqrt(
        (node_lat - destination_lat) ** 2
        + (node_lon - destination_lon) ** 2
    )


def a_star(graph: Graph, start, destination):
    """
    Find the shortest path between two nodes using A*.

    Returns:
        tuple:
            shortest_distance
            shortest_path
    """

    if start not in graph.get_nodes():
        raise ValueError(f"Start node '{start}' does not exist.")

    if destination not in graph.get_nodes():
        raise ValueError(
            f"Destination node '{destination}' does not exist."
        )

    distances = {
        node: float("inf")
        for node in graph.get_nodes()
    }

    previous = {
        node: None
        for node in graph.get_nodes()
    }

    distances[start] = 0

    priority_queue = PriorityQueue()
    priority_queue.push(
        heuristic(graph, start, destination),
        start,
    )

    while not priority_queue.is_empty():

        current_priority, current_node = priority_queue.pop()

        current_distance = distances[current_node]

        if current_node == destination:
            break

        for neighbor, weight in graph.get_neighbors(current_node):

            new_distance = current_distance + weight

            if new_distance < distances[neighbor]:

                distances[neighbor] = new_distance
                previous[neighbor] = current_node

                estimated_total = (
                    new_distance
                    + heuristic(graph, neighbor, destination)
                )

                priority_queue.push(
                    estimated_total,
                    neighbor,
                )

    if distances[destination] == float("inf"):
        return float("inf"), []

    path = []
    current = destination

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()

    return distances[destination], path