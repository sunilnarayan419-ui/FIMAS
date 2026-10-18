def best_so_far(values: list[float], minimize: bool = True) -> list[float]:
    """Return cumulative best objective values over an optimization trace."""
    result: list[float] = []
    current: float | None = None
    for value in values:
        current = value if current is None else (
            min(current, value) if minimize else max(current, value)
        )
        result.append(current)
    return result
