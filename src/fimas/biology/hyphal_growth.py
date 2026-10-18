import networkx as nx


def add_hyphal_edge(
    graph: nx.Graph, source: str, target: str, conductance: float = 1.0
) -> None:
    """Add a candidate hyphal connection to a graph.

    This is a minimal graph operation, not a biologically validated growth model.
    """
    if conductance < 0:
        raise ValueError("conductance must be non-negative")
    graph.add_edge(source, target, conductance=conductance, active=True)
