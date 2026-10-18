def transfer_resource(
    available: float, requested: float, maximum_transfer: float | None = None
) -> float:
    """Return a feasible transfer amount without changing agent state."""
    if available < 0 or requested < 0:
        raise ValueError("Available and requested resources must be non-negative")
    limit = available if maximum_transfer is None else maximum_transfer
    if limit < 0:
        raise ValueError("maximum_transfer must be non-negative")
    return min(available, requested, limit)
