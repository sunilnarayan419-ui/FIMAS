from dataclasses import dataclass


@dataclass(frozen=True)
class ResourceState:
    available: float
    allocated: float = 0.0

    def __post_init__(self) -> None:
        if self.available < 0 or self.allocated < 0:
            raise ValueError("Resource quantities must be non-negative.")
        if self.allocated > self.available:
            raise ValueError("Allocated resources cannot exceed available resources.")
