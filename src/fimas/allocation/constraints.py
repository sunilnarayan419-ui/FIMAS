def allocation_is_feasible(
    supply: float, demands: dict[str, float], allocations: dict[str, float], tolerance: float = 1e-9
) -> bool:
    """Check non-negativity, demand bounds, and aggregate supply feasibility."""
    if supply < 0 or tolerance < 0:
        return False
    if set(demands) != set(allocations):
        return False
    if any(value < -tolerance for value in allocations.values()):
        return False
    if any(demands[key] < 0 for key in demands):
        return False
    if any(allocations[key] > demands[key] + tolerance for key in demands):
        return False
    return sum(allocations.values()) <= supply + tolerance
