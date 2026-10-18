from dataclasses import dataclass
import networkx as nx


@dataclass
class NetworkState:
    graph: nx.Graph
    time_step: int = 0

    def __post_init__(self) -> None:
        if self.time_step < 0:
            raise ValueError("time_step must be non-negative.")
