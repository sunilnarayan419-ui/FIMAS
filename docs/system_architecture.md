# System Architecture

The intended architecture separates:
- Python scientific core: graph models, resource flow, optimization, simulation, and metrics.
- FastAPI interface: typed access to simulation functions when needed.
- TypeScript services: market event processing and interactive visualization.
- Contracts: schemas shared across service boundaries.
- Experiment layer: configurations, seeds, protocols, and result provenance.

Implement and validate the Python core before adding distributed infrastructure.
