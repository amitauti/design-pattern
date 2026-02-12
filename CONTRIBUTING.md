# Contributing

Thanks for contributing! Please follow these guidelines based on the AI Design & Architecture Patterns Reference Guide:

## Creating New Patterns

- Choose an appropriate category from our [taxonomy](docs/TAXONOMY.md):
  - System Architecture Patterns (microservices, agent-based, event-driven)
  - ML Pipeline Architecture Patterns (DAGs, shared-nothing, parameter server)
  - Deployment Patterns (online/batch serving, blue-green, canary)
  - Scalability Patterns (horizontal/vertical scaling, load balancing)
  - Data Patterns (feature store, data versioning, stream processing)
  - Model Serving Patterns (model registry, multi-model, A/B testing)
  - MLOps Patterns (continuous training, monitoring, experiment tracking)
  - Infrastructure Patterns (distributed systems, GPU pooling, edge deployment)
- Create or update a pattern under `patterns/high-level` or `patterns/low-level`.
- Use `templates/pattern-template.md` for new pattern pages, ensuring all sections are completed: Summary, Problem, Context, Solution, System Architecture Considerations, ML Pipeline Architecture, Deployment Strategy, Scalability Approach, Data Handling, Model Serving, MLOps Integration, Infrastructure Requirements, Diagram(s), Examples, References, Guardrails, Monitoring, Governance, Security, Testing, Reproducibility, Lifecycle, and Delivery Checklist.

## Pattern Requirements

When creating a new pattern, ensure it addresses:

- **System Architecture Considerations**: How does it fit into microservices, agent-based, or event-driven architectures?
- **ML Pipeline Integration**: How does it work with DAGs, shared-nothing, or distributed learning architectures?
- **Deployment Strategy**: Is it suited for online/batch serving, blue-green, or canary deployments?
- **Scalability Approach**: How does it scale horizontally or vertically?
- **Data Handling**: How does it interact with feature stores, data versioning, or stream processing?
- **Model Serving**: How does it work with model registries, multi-model serving, or A/B testing?
- **MLOps Integration**: How does it support continuous training, monitoring, or experiment tracking?
- **Infrastructure Requirements**: What infrastructure does it need (distributed systems, GPU resources, edge deployment)?

## Technical Requirements

- Include at least one diagram in Mermaid or PlantUML format.
- Provide concrete examples and code snippets where applicable.
- Include relevant references to research papers, articles, or best practices.
- Address security, monitoring, and governance considerations.
- Follow the style guide in `docs/STYLE_GUIDE.md`.

## Pull Requests

- Open a PR with a descriptive title and link to related issues.
- Ensure all sections of the pattern template are thoughtfully completed.
- Verify that the pattern aligns with our taxonomy and follows best practices.
- Include any relevant diagrams or code examples.

## Review Process

Pattern submissions will be reviewed for:
- Alignment with established architecture patterns
- Completeness of all required sections
- Practical applicability and real-world relevance
- Adherence to security, monitoring, and governance best practices
- Quality of examples and diagrams
