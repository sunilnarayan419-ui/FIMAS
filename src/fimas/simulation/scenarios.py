def edge_failure_fraction(edge_count: int, failure_fraction: float) -> int:
    """Return the number of edges to remove for a requested fraction, rounded down."""
    if edge_count < 0 or not 0 <= failure_fraction <= 1:
        raise ValueError("edge_count must be non-negative and fraction in [0, 1]")
    return int(edge_count * failure_fraction)
