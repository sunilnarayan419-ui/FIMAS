import networkx as nx


def is_connected(graph: nx.Graph) -> bool:
    """Return connectivity for an undirected graph; an empty graph is not connected."""
    return bool(graph.number_of_nodes()) and nx.is_connected(graph)
