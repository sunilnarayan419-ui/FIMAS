def total_unmet_demand(demands: dict[str, float], allocations: dict[str, float]) -> float:
    """Return aggregate unmet demand for matching demand/allocation mappings."""
    if set(demands) != set(allocations):
        raise ValueError("Demand and allocation keys must match")
    if any(value < 0 for value in demands.values()) or any(
        value < 0 for value in allocations.values()
    ):
        raise ValueError("Demands and allocations must be non-negative")
    return sum(max(0.0, demand - allocations[key]) for key, demand in demands.items())
