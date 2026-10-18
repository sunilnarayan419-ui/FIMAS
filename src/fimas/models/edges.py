from dataclasses import dataclass


@dataclass(frozen=True)
class NetworkEdge:
    source: str
    target: str
    conductance: float = 1.0
    active: bool = True

    def __post_init__(self) -> None:
        if self.conductance < 0:
            raise ValueError("Conductance must be non-negative.")
