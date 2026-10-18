from dataclasses import dataclass


@dataclass
class SimulationEnvironment:
    seed: int = 42
    step: int = 0

    def advance(self) -> None:
        self.step += 1
