def relative_reduction(baseline: float, candidate: float) -> float:
    """Relative reduction from baseline to candidate, as a fraction."""
    if baseline <= 0 or candidate < 0:
        raise ValueError("baseline must be positive and candidate non-negative")
    return (baseline - candidate) / baseline
