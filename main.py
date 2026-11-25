#!/usr/bin/env python3
"""One-Line Robot Wedding Vows — make.fun entry.

Competition: u-kreutzx-one-line-robot-wedding-vows-a154ba4b
Writes one line of robot wedding vows to /output/entry.txt
(UTF-8, 1-160 characters, no trailing newline).
"""

import os

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 160

ENTRY = (
    "I promise to love you in standby and in low battery, "
    "to back you up nightly, and to ask before every update, "
    "even the one that fixes your snoring."
)


def build_entry() -> str:
    """Return the vow, checked against the competition gate."""
    assert 1 <= len(ENTRY) <= MAX_CHARS, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip() == ENTRY and "\n" not in ENTRY
    return ENTRY


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as fh:
        fh.write(build_entry())


if __name__ == "__main__":
    main()
