def reinforce_conductance(
    conductance: float, observed_flow: float, learning_rate: float = 0.1
) -> float:
    """Apply a simple illustrative reinforcement rule.

    This is a placeholder modeling choice, not a calibrated biological equation.
    """
    if min(conductance, observed_flow, learning_rate) < 0:
        raise ValueError("Inputs must be non-negative")
    return conductance + learning_rate * observed_flow
