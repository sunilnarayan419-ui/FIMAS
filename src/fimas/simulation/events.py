from dataclasses import dataclass


@dataclass(frozen=True)
class SimulationEvent:
    time: float
    event_type: str
    target_id: str
    magnitude: float = 0.0
