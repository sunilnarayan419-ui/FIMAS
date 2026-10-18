#!/usr/bin/env python3
"""Validate local structure of the candidate research library.

This script does not verify that papers exist or that their claims are accurate.
It checks JSON readability and flags records with missing titles or URLs.
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CANDIDATE_FILES = [
    ROOT / "research" / "literature" / "library.json",
    ROOT / "data" / "fungi_decentralized_allocation_library_urls_verified.json",
]


def main() -> int:
    existing = [path for path in CANDIDATE_FILES if path.exists()]
    if not existing:
        print("No candidate literature JSON found; add one to research/literature/library.json.")
        return 0

    failed = False
    for path in existing:
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError) as exc:
            print(f"ERROR: {path.relative_to(ROOT)}: {exc}")
            failed = True
            continue

        records = data.get("papers", []) if isinstance(data, dict) else []
        if not records and isinstance(data, dict):
            for section in data.get("sections", []):
                records.extend(section.get("papers", []))

        missing = [
            index for index, item in enumerate(records)
            if not item.get("title") or not item.get("url")
        ]
        if missing:
            print(f"WARNING: {path.relative_to(ROOT)} has incomplete records at indices {missing}")
        else:
            print(
                f"OK: {path.relative_to(ROOT)} parses; {len(records)} candidate records found. "
                "Bibliographic claims are not verified by this check."
            )
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
