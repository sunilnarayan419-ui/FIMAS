PYTHON ?= python
UV ?= uv

.PHONY: install test lint format typecheck run validate-refs

install:
	$(UV) sync --dev

test:
	$(UV) run pytest

lint:
	$(UV) run ruff check .

format:
	$(UV) run ruff format .

typecheck:
	$(UV) run mypy src

run:
	$(UV) run python scripts/run_simulation.py

validate-refs:
	$(UV) run python scripts/validate_references.py
