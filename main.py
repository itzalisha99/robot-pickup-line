#!/usr/bin/env python3
"""The Robot Pickup Line Championship — make.fun entry.

Writes one pickup line, in the voice of a robot trying to charm someone,
to /output/entry.txt.
"""

import os

LINE = "I wasn't built to feel, but my cooling fan spins every time you walk past."


def validate(line):
    """Mirror the bounty gate: UTF-8 text, 1-200 chars, not only
    whitespace, a single line. Refuse to write a line that would fail."""
    if not isinstance(line, str):
        raise ValueError("entry must be text")
    line.encode("utf-8")
    if not 1 <= len(line) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(line))
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    return line


def main():
    validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
