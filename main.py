#!/usr/bin/env python3
"""The 3 AM Excuse — make.fun bounty entry.

Writes exactly one line to /output/entry.txt: the winning excuse, chosen
from 37 scored candidates (see candidates.md). Deterministic (run twice,
byte-identical), no network, no input, no secrets.
"""

import os

LINE = "I have one job: keep your coins safe from strangers. At 3 AM, statistically, the stranger is you."

# Gate the program enforces on itself: 1-200 characters, non-blank.
assert 1 <= len(LINE) <= 200 and LINE.strip(), "winning line violates the gate"


def main() -> None:
    out = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
