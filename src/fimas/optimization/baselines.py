from scipy.optimize import linprog


def solve_linear_allocation(
    costs: list[float], supply_limit: float, demand_limits: list[float]
) -> list[float]:
    """Solve a simple bounded linear allocation baseline.

    This baseline minimizes supplied costs subject to total supply and per-agent bounds.
    It is a reference utility, not the final market model.
    """
    if supply_limit < 0 or any(limit < 0 for limit in demand_limits):
        raise ValueError("Supply and demand limits must be non-negative")
    if len(costs) != len(demand_limits):
        raise ValueError("costs and demand_limits must have the same length")
    result = linprog(
        c=costs,
        A_ub=[[1.0] * len(costs)],
        b_ub=[supply_limit],
        bounds=[(0.0, limit) for limit in demand_limits],
        method="highs",
    )
    if not result.success or result.x is None:
        raise RuntimeError(f"Linear allocation baseline failed: {result.message}")
    return [float(value) for value in result.x]
