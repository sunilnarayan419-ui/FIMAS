def conservation_error(inflow: float, outflow: float, accumulation: float = 0.0) -> float:
    """Return mass-balance residual: inflow - outflow - accumulation."""
    return inflow - outflow - accumulation
