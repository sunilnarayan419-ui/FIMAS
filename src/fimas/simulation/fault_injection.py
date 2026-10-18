import random
import networkx as nx


def remove_random_edges(graph: nx.Graph, fraction: float, seed: int = 42) -> nx.Graph:
    """Return a copy of graph with a seeded fraction of edges removed."""
    if not 0 <= fraction <= 1:
        raise ValueError("fraction must be in [0, 1]")
    damaged = graph.copy()
    edge_list = list(damaged.edges())
    count = int(len(edge_list) * fraction)
    chosen = random.Random(seed).sample(edge_list, count)
    damaged.remove_edges_from(chosen)
    return damaged
