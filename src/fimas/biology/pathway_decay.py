def decay_conductance(conductance: float, decay_rate: float) -> float:
    """Apply multiplicative decay to an underused pathway's conductance."""
    if conductance < 0 or not 0 <= decay_rate <= 1:
        raise ValueError("conductance must be non-negative and decay_rate in [0, 1]")
    return conductance * (1.0 - decay_rate)
