# Patterns Index

This index lists available patterns in the repository, organized by category based on the AI Design & Architecture Patterns Reference Guide.

## System Architecture Patterns

- Microservices Architecture (high): `patterns/high-level/microservices-architecture.md` — containerized services with isolated components for reliable AI deployment.
- Agent-Based Architecture (high): `patterns/high-level/agent-based-architecture.md` — multi-agent coordination with shared memory systems.
- Event-Driven Architecture (high): `patterns/high-level/event-driven-architecture.md` — reactive processing for enhanced efficiency and scalability.

## ML Pipeline Architecture Patterns

- Directed Acyclic Graphs (DAGs) (high): `patterns/high-level/dag-workflows.md` — structured workflows with clear dependencies for ML pipelines.
- Shared-Nothing Architecture (high): `patterns/high-level/shared-nothing-architecture.md` — horizontally scalable independent processing.
- Parameter Server Architecture (high): `patterns/high-level/parameter-server-architecture.md` — coordinated parameter management for distributed learning.
- Ring-AllReduce Architecture (high): `patterns/high-level/ring-allreduce-architecture.md` — efficient gradient aggregation across nodes.

## Deployment Patterns

- Online Serving (high): `patterns/high-level/online-serving.md` — real-time inference for low-latency applications.
- Batch Serving (high): `patterns/high-level/batch-serving.md` — scheduled bulk processing for non-critical workloads.
- Blue/Green Deployments (high): `patterns/high-level/blue-green-deployments.md` — zero-downtime deployments with instant rollback.
- Canary Deployments (high): `patterns/high-level/canary-deployments.md` — progressive rollout for safe model releases.

## Scalability Patterns

- Horizontal Scaling (high): `patterns/high-level/horizontal-scaling.md` — adding instances for linear scalability.
- Vertical Scaling (high): `patterns/high-level/vertical-scaling.md` — increasing resources for intensive tasks.
- Load Balancing & Auto-Scaling (high): `patterns/high-level/load-balancing-auto-scaling.md` — dynamic capacity adjustment.

## Data Patterns

- Feature Store Pattern (high): `patterns/high-level/feature-store-pattern.md` — centralized feature management.
- Data Versioning Pattern (high): `patterns/high-level/data-versioning-pattern.md` — track datasets for reproducibility.
- Stream Processing Pattern (high): `patterns/high-level/stream-processing-pattern.md` — real-time data ingestion and processing.

## Model Serving Patterns

- Model Registry Pattern (high): `patterns/high-level/model-registry-pattern.md` — centralized model lifecycle management.
- Multi-Model Serving (high): `patterns/high-level/multi-model-serving.md` — efficient resource utilization.
- A/B Testing Pattern (high): `patterns/high-level/a-b-testing-pattern.md` — performance comparison of model variants.
- Shadow Mode Pattern (high): `patterns/high-level/shadow-mode-pattern.md` — risk-free model validation.

## MLOps Patterns

- Continuous Training (CT) (high): `patterns/high-level/continuous-training.md` — automated retraining pipelines.
- Model Monitoring Pattern (high): `patterns/high-level/model-monitoring-pattern.md` — comprehensive production monitoring.
- Experiment Tracking Pattern (high): `patterns/high-level/experiment-tracking-pattern.md` — systematic experiment recording.
- Model Governance Pattern (high): `patterns/high-level/model-governance-pattern.md` — regulatory and compliance assurance.

## Infrastructure Patterns

- Distributed AI Superfactories (high): `patterns/high-level/distributed-ai-superfactories.md` — global distributed computing resources.
- GPU Resource Pooling (high): `patterns/high-level/gpu-resource-pooling.md` — shared GPU infrastructure.
- Edge Deployment Pattern (high): `patterns/high-level/edge-deployment-pattern.md` — low-latency deployment closer to users.

## Existing Patterns

- Model Deployment (high): `patterns/high-level/model-deployment.md` — strategies for serving and rolling out models.
- Data Pipeline (high): `patterns/high-level/data-pipeline.md` — ingestion, validation, and transformation pipelines.
- Feature Store (high): `patterns/high-level/feature-store.md` — design and trade-offs of feature stores.
- Training Loop (low): `patterns/low-level/training-loop.md` — resilient training loop patterns.
- Data Augmentation (low): `patterns/low-level/data-augmentation.md` — reproducible augmentation strategies.
- Optimizer Pattern (low): `patterns/low-level/optimizer-pattern.md` — optimizer/scheduler factories.

Use `templates/pattern-template.md` when adding new patterns.
