def allocate_proportionally(supply: float, demands: dict[str, float]) -> dict[str, float]:
    """Allocate a single resource proportionally to non-negative demands."""
    if supply < 0 or any(demand < 0 for demand in demands.values()):
        raise ValueError("Supply and demands must be non-negative")
    total_demand = sum(demands.values())
    if total_demand == 0:
        return {agent: 0.0 for agent in demands}
    allocated_total = min(supply, total_demand)
    return {
        agent: allocated_total * demand / total_demand
        for agent, demand in demands.items()
    }
