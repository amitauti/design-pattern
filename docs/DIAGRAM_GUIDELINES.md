# Diagram Guidelines

Guidelines for creating and storing diagrams in this repository.

## Mermaid

- Store small examples inline in pattern markdown using fenced ```mermaid blocks.
- For reusable diagrams, add `.mmd` files under `diagrams/mermaid/` and reference them.
- Keep graphs simple; prefer top-down (`graph TD`) for architectures.

## PlantUML

- Use `.puml` files under `diagrams/plantuml/` for complex sequence or component diagrams.
- Keep diagrams parameterized by annotations when useful.

## Naming

- Use descriptive names with kebab-case: `pipeline-batch.mmd`, `model-rollout.puml`.
