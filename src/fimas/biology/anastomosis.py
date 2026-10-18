import networkx as nx


def fuse_paths(graph: nx.Graph, source: str, target: str, conductance: float = 1.0) -> None:
    """Represent a path-fusion event as an edge addition.

    Compatibility rules and biological calibration are not implemented yet.
    """
    if conductance < 0:
        raise ValueError("conductance must be non-negative")
    graph.add_edge(source, target, conductance=conductance, anastomosis=True, active=True)
