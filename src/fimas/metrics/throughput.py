def throughput(delivered: float, duration: float) -> float:
    if delivered < 0 or duration <= 0:
        raise ValueError("delivered must be non-negative and duration positive")
    return delivered / duration
