def uniform_price(marginal_cost: float, scarcity_premium: float = 0.0) -> float:
    """Illustrative price rule; not an equilibrium or market-clearing solver."""
    if marginal_cost < 0 or scarcity_premium < 0:
        raise ValueError("Price components must be non-negative")
    return marginal_cost + scarcity_premium
