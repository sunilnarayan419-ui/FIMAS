import networkx as nx
import pytest

from fimas.allocation.allocator import allocate_proportionally
from fimas.allocation.fairness import jains_fairness_index
from fimas.biology.pathway_decay import decay_conductance
from fimas.metrics.throughput import throughput
from fimas.network.resilience import largest_component_fraction
from fimas.network.topology import make_path_graph
from fimas.physics.conservation import conservation_error
from fimas.simulation.fault_injection import remove_random_edges


def test_path_graph_has_expected_edges() -> None:
    graph = make_path_graph(5)
    assert graph.number_of_nodes() == 5
    assert graph.number_of_edges() == 4


def test_empty_graph_resilience_is_zero() -> None:
    assert largest_component_fraction(nx.Graph()) == 0.0


def test_fault_injection_is_reproducible() -> None:
    graph = make_path_graph(20)
    first = remove_random_edges(graph, 0.4, seed=123)
    second = remove_random_edges(graph, 0.4, seed=123)
    assert set(first.edges()) == set(second.edges())


def test_proportional_allocation_respects_supply() -> None:
    result = allocate_proportionally(10, {"a": 8, "b": 12})
    assert sum(result.values()) == pytest.approx(10)
    assert result["a"] == pytest.approx(4)
    assert result["b"] == pytest.approx(6)


def test_jain_index_equal_allocation_is_one() -> None:
    assert jains_fairness_index([5, 5, 5]) == pytest.approx(1.0)


def test_decay_reduces_conductance() -> None:
    assert decay_conductance(10, 0.2) == pytest.approx(8.0)


def test_throughput_units() -> None:
    assert throughput(100, 5) == pytest.approx(20.0)


def test_conservation_residual() -> None:
    assert conservation_error(10, 7, 3) == pytest.approx(0.0)
