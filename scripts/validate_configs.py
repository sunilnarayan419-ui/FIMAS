#!/usr/bin/env python3
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    paths = sorted((ROOT / "configs").rglob("*.yaml"))
    for path in paths:
        with path.open(encoding="utf-8") as handle:
            yaml.safe_load(handle)
        print(f"OK {path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
