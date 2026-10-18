import networkx as nx


def largest_component_fraction(graph: nx.Graph) -> float:
    """Fraction of nodes in the largest connected component; 0 for an empty graph."""
    if graph.number_of_nodes() == 0:
        return 0.0
    largest = max(len(component) for component in nx.connected_components(graph))
    return largest / graph.number_of_nodes()
