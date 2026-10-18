from dataclasses import dataclass


@dataclass
class MarketAgent:
    agent_id: str
    endowment: float
    demand: float

    def __post_init__(self) -> None:
        if self.endowment < 0 or self.demand < 0:
            raise ValueError("Endowment and demand must be non-negative")
