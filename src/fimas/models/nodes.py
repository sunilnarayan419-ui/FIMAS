from dataclasses import dataclass


@dataclass(frozen=True)
class ResourceNode:
    node_id: str
    supply: float = 0.0
    demand: float = 0.0
    capacity: float = float("inf")

    def __post_init__(self) -> None:
        if self.supply < 0 or self.demand < 0 or self.capacity < 0:
            raise ValueError("Supply, demand, and capacity must be non-negative.")
