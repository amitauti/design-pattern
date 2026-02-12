# Taxonomy

This document defines the taxonomy used across the repository for classifying patterns, artifacts and diagrams.

## Levels

- High-level: architecture and system-level patterns (cross-service, infra, ops).
- Low-level: implementation patterns (code-level, algorithms, training specifics).

## Pattern Metadata

Each pattern page should include front-matter keys:

- `title`: short human-friendly title
- `level`: `high` or `low`
- `tags`: list of short tags (e.g., `training`, `serving`, `data`)

## Diagram Types

- Mermaid: architecture and sequence diagrams for quick rendering.
- PlantUML: richer UML-style diagrams and printable diagrams.
