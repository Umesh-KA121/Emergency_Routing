class Graph:
    """
    Weighted graph representation of the emergency road network.
    """

    def __init__(self):
        self.graph = {}
        self.coordinates = {}

    def add_node(self, node, latitude=None, longitude=None):
        """Add a node and optionally store its coordinates."""

        if node not in self.graph:
            self.graph[node] = []

        if latitude is not None and longitude is not None:
            self.coordinates[node] = (latitude, longitude)

    def add_edge(self, source, destination, weight, bidirectional=True):
        """Add a weighted edge to the graph."""

        if weight < 0:
            raise ValueError("Edge weight cannot be negative.")

        self.add_node(source)
        self.add_node(destination)

        self.graph[source].append((destination, weight))

        if bidirectional:
            self.graph[destination].append((source, weight))

    def get_neighbors(self, node):
        """Return neighboring nodes and their edge weights."""

        return self.graph.get(node, [])

    def get_nodes(self):
        """Return all nodes in the graph."""

        return list(self.graph.keys())

    def get_coordinates(self, node):
        """Return coordinates for a node."""

        return self.coordinates.get(node)