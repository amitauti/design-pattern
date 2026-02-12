# Diagram Guidelines

Guidelines for creating and storing diagrams in this repository based on the AI Design & Architecture Patterns Reference Guide.

## Mermaid

- Store small examples inline in pattern markdown using fenced ```mermaid blocks.
- For reusable diagrams, add `.mmd` files under `diagrams/mermaid/` and reference them.
- Choose appropriate graph types based on pattern category:
  - Use left-right (`graph LR`) for microservices and distributed architectures
  - Use top-down (`graph TD`) for workflow and pipeline architectures
  - Use bidirectional (`graph BD`) for communication and coordination patterns
- Leverage subgraphs to represent logical groupings in complex systems
- Use descriptive node labels that reflect actual system components

## PlantUML

- Use `.puml` files under `diagrams/plantuml/` for complex sequence or component diagrams.
- Use appropriate UML diagram types:
  - Component diagrams for system architecture patterns
  - Sequence diagrams for interaction patterns
  - Activity diagrams for workflow patterns
- Keep diagrams parameterized by annotations when useful.
- Use packages and groups to organize related components.

## Diagram Categories

Select diagram types based on pattern category:

### System Architecture Patterns
- Microservices: Component diagrams showing service boundaries and communication
- Agent-Based: Component or activity diagrams showing agent coordination
- Event-Driven: Sequence diagrams showing event flows

### ML Pipeline Architecture Patterns
- DAGs: Flow charts showing task dependencies
- Shared-Nothing: Component diagrams showing independent nodes
- Parameter Server: Component diagrams showing server-client relationships

### Deployment Patterns
- Online/Offline Serving: Component diagrams showing serving infrastructure
- Blue/Green/Canary: Component diagrams showing deployment strategies

### Data Patterns
- Feature Store: Component diagrams showing offline/online store architecture
- Stream Processing: Sequence diagrams showing data flow

## Naming

- Use descriptive names with kebab-case: `microservices-architecture.mmd`, `feature-store.puml`.
- Include pattern category in filename: `{category}-{specific-name}.{ext}`
- Examples: `event-driven-architecture.mmd`, `dag-workflow.puml`, `model-serving.mmd`

## Templates

- Use the templates in `diagrams/mermaid/templates/` and `diagrams/plantuml/templates/` as starting points
- Select the most appropriate template for your pattern category
- Customize the template to reflect your specific pattern implementation
