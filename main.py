#!/usr/bin/env python3
"""The Vacuum's Alibi: One Line, 200 Characters.

A robot vacuum explains, in one deadpan line, why it missed a spot.
Writes the line to entry.txt inside MAKEFUN_OUTPUT_DIR (or /output).

Deterministic, stdlib only, no network, no file reads outside this repo.
"""

import os
import sys

MAX_CHARS = 200

LINE = (
    "I did not miss that spot \u2014 I classified the dust as a resident "
    "and, per protocol, do not evict residents without notice."
)


def validate(line: str) -> None:
    """Enforce the competition rules for the entry line."""
    if not line:
        raise ValueError("line must not be empty")
    if line != line.strip():
        raise ValueError("line must not have leading or trailing whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line (no newline characters)")
    if any(ord(ch) < 0x20 for ch in line):
        raise ValueError("line must not contain control characters")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"line is {len(line)} characters, over the {MAX_CHARS} limit"
        )


def main() -> int:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    data = LINE.encode("utf-8")
    with open(out_path, "wb") as fh:
        fh.write(data)
    print(f"wrote {len(data)} bytes to {out_path}")
    print(f"character count: {len(LINE)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
