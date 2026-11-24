#!/usr/bin/env python3
"""Copy the dual-host plugin into a new or empty repository directory."""
from __future__ import annotations

import argparse
import shutil
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destination", type=Path, help="new or empty repository directory")
    args = parser.parse_args()
    source = Path(__file__).resolve().parents[3]
    destination = args.destination.resolve()
    if destination.exists():
        allowed = {".git"}
        existing = {p.name for p in destination.iterdir()}
        if existing - allowed:
            parser.error(f"refusing to overwrite non-empty destination: {destination}")
    else:
        destination.mkdir(parents=True)
    target = destination / "plugins" / "content-studio"
    if target.exists():
        parser.error(f"refusing to overwrite: {target}")
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, target, ignore=shutil.ignore_patterns("__pycache__", ".DS_Store"))
    print(f"Exported dual-host plugin to {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
