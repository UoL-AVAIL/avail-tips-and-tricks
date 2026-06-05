#!/usr/bin/env python3
"""Template utility script.

Purpose:
- Describe what this script does.

Inputs:
- Define required inputs and flags.

Outputs:
- Define generated files or console output.

Dependencies:
- List required Python packages.

Example usage:
- python scripts/your_script.py --input data/input.csv --output data/output.csv
"""

import argparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Template utility script")
    parser.add_argument("--input", required=True, help="Path to input file")
    parser.add_argument("--output", required=True, help="Path to output file")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    with open(args.output, "w", encoding="utf-8") as handle:
        handle.write(f"Processed {args.input}\n")


if __name__ == "__main__":
    main()
