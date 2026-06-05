# Getting Started with W&B

**Last updated:** 2026-06-05

## Purpose

Track basic experiment metrics and compare runs.

## Quick start

1. Install: `pip install wandb`
2. Login: `wandb login`
3. In your training script, initialise a run and log metrics.

```python
import wandb
wandb.init(project="avail-demo")
wandb.log({"loss": 0.42, "epoch": 1})
```

## AVAIL usage tip

Use consistent run names and tags (for example module, dataset, seed) so results are easier to compare.
