class Graph:
    """
    Weighted graph representation of the emergency road network.
    """

    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        """Add a node if it does not already exist."""
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, source, destination, weight):
        """Add a weighted directed edge."""
        self.add_node(source)
        self.add_node(destination)

        self.graph[source].append((destination, weight))

    def get_neighbors(self, node):
        """Return neighboring nodes and their edge weights."""
        return self.graph.get(node, [])

    def get_nodes(self):
        """Return all nodes in the graph."""
        return list(self.graph.keys())