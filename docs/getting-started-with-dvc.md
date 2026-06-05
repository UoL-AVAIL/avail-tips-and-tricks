# Getting Started with DVC

**Last updated:** 2026-06-05

## Purpose

Version datasets and derived artefacts alongside code.

## Quick start

1. Install: `pip install dvc`
2. Initialise in repository root: `dvc init`
3. Track a data file: `dvc add data/raw.csv`
4. Commit generated `.dvc` files and `.gitignore` updates.

## AVAIL usage tip

Use DVC for large data and intermediate outputs; keep scripts and documentation in Git for full reproducibility context.
