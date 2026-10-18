def jains_fairness_index(values: list[float]) -> float:
    """Calculate Jain's fairness index for non-negative allocations or utilities."""
    if any(value < 0 for value in values):
        raise ValueError("Values must be non-negative")
    if not values or sum(value * value for value in values) == 0:
        return 0.0
    total = sum(values)
    return (total * total) / (len(values) * sum(value * value for value in values))
