# ADR 0002: No Notebook Workflow

## Status
Accepted.

## Decision
Use ordinary Python modules, command-line scripts, configuration files, tests, and Markdown
reports. Do not make Jupyter or Google Colab notebooks part of the workflow.

## Rationale
Script-based execution is easier to review, test, version, automate, and reproduce in CI.
