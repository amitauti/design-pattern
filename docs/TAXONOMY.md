# Taxonomy

This document defines the taxonomy used across the repository for classifying patterns, artifacts and diagrams, based on the AI Design & Architecture Patterns Reference Guide.

## Categories

Patterns are organized into the following categories:

### System Architecture Patterns
- Microservices Architecture: Containerized services with isolated components
- Agent-Based Architecture: Multi-agent coordination with shared memory systems
- Event-Driven Architecture: Reactive processing for enhanced efficiency

### ML Pipeline Architecture Patterns
- Directed Acyclic Graphs (DAGs): Structured workflows with clear dependencies
- Shared-Nothing Architecture: Horizontally scalable independent processing
- Parameter Server Architecture: Coordinated parameter management for distributed learning
- Ring-AllReduce Architecture: Efficient gradient aggregation across nodes

### Deployment Patterns
- Online Serving: Real-time inference for low-latency applications
- Batch Serving: Scheduled bulk processing for non-critical workloads
- Blue/Green Deployments: Zero-downtime deployments with instant rollback
- Canary Deployments: Progressive rollout for safe model releases

### Scalability Patterns
- Horizontal Scaling: Adding instances for linear scalability
- Vertical Scaling: Increasing resources for intensive tasks
- Load Balancing & Auto-Scaling: Dynamic capacity adjustment

### Data Patterns
- Feature Store Pattern: Centralized feature management
- Data Versioning Pattern: Track datasets for reproducibility
- Stream Processing Pattern: Real-time data ingestion and processing

### Model Serving Patterns
- Model Registry Pattern: Centralized model lifecycle management
- Multi-Model Serving: Efficient resource utilization
- A/B Testing Pattern: Performance comparison of model variants
- Shadow Mode Pattern: Risk-free model validation

### MLOps Patterns
- Continuous Training (CT): Automated retraining pipelines
- Model Monitoring Pattern: Comprehensive production monitoring
- Experiment Tracking Pattern: Systematic experiment recording
- Model Governance Pattern: Regulatory and compliance assurance

### Infrastructure Patterns
- Distributed AI Superfactories: Global distributed computing resources
- GPU Resource Pooling: Shared GPU infrastructure
- Edge Deployment Pattern: Low-latency deployment closer to users

## Levels

- High-level: architecture and system-level patterns (cross-service, infra, ops).
- Low-level: implementation patterns (code-level, algorithms, training specifics).

## Pattern Metadata

Each pattern page should include front-matter keys:

- `title`: short human-friendly title
- `level`: `high` or `low`
- `category`: one of the categories listed above
- `tags`: list of short tags (e.g., `training`, `serving`, `data`, `scalability`)

## Diagram Types

- Mermaid: architecture and sequence diagrams for quick rendering.
- PlantUML: richer UML-style diagrams and printable diagrams.
