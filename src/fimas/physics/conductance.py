def edge_flow(conductance: float, potential_difference: float) -> float:
    """Compute a linear edge-flow proxy: flow = conductance * potential difference."""
    if conductance < 0:
        raise ValueError("conductance must be non-negative")
    return conductance * potential_difference
