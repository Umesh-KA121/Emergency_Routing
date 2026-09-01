from app.services.dsa.graph import Graph
from app.services.dsa.priority_queue import PriorityQueue


def dijkstra(graph: Graph, start, destination):
    """
    Find the shortest path between two nodes using Dijkstra's algorithm.

    Returns:
        tuple:
            shortest_distance
            shortest_path
    """

    if start not in graph.get_nodes():
        raise ValueError(f"Start node '{start}' does not exist.")

    if destination not in graph.get_nodes():
        raise ValueError(f"Destination node '{destination}' does not exist.")

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
    priority_queue.push(0, start)

    while not priority_queue.is_empty():

        current_distance, current_node = priority_queue.pop()

        # Ignore outdated entries.
        if current_distance > distances[current_node]:
            continue

        # Destination reached with shortest known distance.
        if current_node == destination:
            break

        for neighbor, weight in graph.get_neighbors(current_node):

            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node

                priority_queue.push(distance, neighbor)

    if distances[destination] == float("inf"):
        return float("inf"), []

    path = []
    current = destination

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()

    return distances[destination], path