# Experiment Tracking Walkthrough

## Purpose

Show a lightweight workflow for tracking experiments with consistent metadata.

## Prerequisites

- Python environment
- A training script that outputs at least one metric

## Steps

1. Create a run name including date and short experiment label.
2. Log core metadata (dataset, model, seed).
3. Log metrics at each epoch.
4. Save a short summary of best result and configuration.

## Common pitfalls

- Missing metadata fields makes runs hard to compare.
- Changing metric names across runs breaks dashboards.

## Further reading

- `docs/getting-started-with-wandb.md`
