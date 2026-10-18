def solve_two_node_flow(
    conductance: float, source_potential: float, sink_potential: float
) -> float:
    """Solve the elementary two-node linear flow relation."""
    if conductance < 0:
        raise ValueError("conductance must be non-negative")
    return conductance * (source_potential - sink_potential)
