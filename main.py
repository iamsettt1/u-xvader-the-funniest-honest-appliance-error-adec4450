#!/usr/bin/env python3
"""The Funniest Honest Appliance Error — make.fun entry.

Writes one line to /output/entry.txt: the funniest honest error message
an appliance could show. Deterministic: the same line every run.
"""

import os

ENTRY = (
    "ERROR E4: UNBALANCED LOAD. "
    "I HAVE REDISTRIBUTED THE TOWELS FOUR TIMES. "
    "THEY KEEP VOTING FOR THE SAME SIDE."
)


def main() -> None:
    # The sealed gate requires 1-200 UTF-8 characters, not only whitespace.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    assert "\n" not in ENTRY and ENTRY.strip(), "entry must be one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
