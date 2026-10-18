#!/usr/bin/env python3
import json
from pathlib import Path

from fimas.network.resilience import largest_component_fraction
from fimas.network.topology import make_path_graph
from fimas.simulation.fault_injection import remove_random_edges

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    graph = make_path_graph(20)
    damaged = remove_random_edges(graph, fraction=0.4, seed=42)
    result = {
        "status": "illustrative_smoke_test",
        "seed": 42,
        "nodes": graph.number_of_nodes(),
        "edges_before": graph.number_of_edges(),
        "edges_after": damaged.number_of_edges(),
        "largest_component_fraction_after": largest_component_fraction(damaged),
        "note": "This is not the full FIMAS model or a KPI validation experiment.",
    }
    output = ROOT / "experiments" / "results" / "smoke_test.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    print(f"Saved: {output.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
