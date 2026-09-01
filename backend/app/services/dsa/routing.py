from app.services.dsa.dijkstra import dijkstra
from app.services.dsa.graph import Graph


class RoutingEngine:
    """
    Routing engine for calculating emergency response routes.

    This class acts as a bridge between the emergency-response
    logic and the underlying DSA algorithms.
    """

    def __init__(self, graph: Graph):
        self.graph = graph

    def find_shortest_route(self, start, destination):
        """
        Find the shortest route between two locations.

        Returns:
            dict containing:
                distance
                path
        """

        distance, path = dijkstra(
            self.graph,
            start,
            destination,
        )

        return {
            "distance": distance,
            "path": path,
        }