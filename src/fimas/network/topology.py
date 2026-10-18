import networkx as nx


def make_path_graph(node_count: int) -> nx.Graph:
    """Create a simple path graph for smoke tests and baseline development."""
    if node_count < 1:
        raise ValueError("node_count must be at least 1")
    return nx.path_graph(node_count)
