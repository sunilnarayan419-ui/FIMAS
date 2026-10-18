from fimas.network.topology import make_path_graph
from fimas.simulation.fault_injection import remove_random_edges


def test_edge_failure_removes_requested_floor_count() -> None:
    graph = make_path_graph(11)  # 10 edges
    damaged = remove_random_edges(graph, 0.4, seed=42)
    assert graph.number_of_edges() - damaged.number_of_edges() == 4
