def equilibrium_residual(excess_supply: float, excess_demand: float) -> float:
    """Return a simple market-clearing residual; equilibrium analysis is not implemented."""
    if excess_supply < 0 or excess_demand < 0:
        raise ValueError("Excess supply and demand magnitudes must be non-negative")
    return excess_supply - excess_demand
