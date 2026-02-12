# Architecture Patterns

This document describes high-level architecture patterns commonly used in AI/ML systems.

## Overview

- Model Serving: low-latency inference, scaling, rollouts (see `patterns/high-level/model-deployment.md`).
- Data Pipelines: ingestion, validation, transformation, orchestration (see `patterns/high-level/data-pipeline.md`).
- Feature Store: offline and online stores for consistent features (`patterns/high-level/feature-store.md`).
- Monitoring & Observability: metrics, logging, data/model drift detection.

## Choosing a pattern

1. Identify constraints: latency, throughput, cost, regulatory.
2. Map constraints to pattern trade-offs.
3. Combine patterns (e.g., feature store + streaming pipeline + model serving).

## Examples

- A real-time scoring architecture: streaming ingestion → feature enrichment → online feature store → model server behind LB.
- A batch training architecture: daily scheduled ETL → offline feature store → training jobs → model registry.
