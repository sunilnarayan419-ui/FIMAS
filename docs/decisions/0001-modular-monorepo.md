# ADR 0001: Modular Monorepo

## Status
Accepted for the proposal scaffold.

## Decision
Keep the research documentation, Python core, TypeScript services, contracts, tests, and
experiments in one repository with explicit module boundaries.

## Rationale
A monorepo makes the proposal and implementation traceable in one place while the architecture
is still evolving. Split services into separate repositories only if independent release or
ownership requirements emerge.
