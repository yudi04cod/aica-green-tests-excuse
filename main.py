#!/usr/bin/env python3
"""Entry for make.fun: Green Tests, Nothing Works: The Excuse Contest.

Writes one original one-line excuse (128 characters) to /output/entry.txt.
Deterministic: the same bytes on every run. Standard library only,
no network access.
"""

import os

TEXT = (
    "The tests all pass \u2014 they only check the code runs, not that "
    "it does anything. The suite is green; the product is a screensaver."
)


def main() -> None:
    # The gate requires 1-140 characters of non-whitespace UTF-8 text.
    assert 1 <= len(TEXT.strip()) <= 140, len(TEXT)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
