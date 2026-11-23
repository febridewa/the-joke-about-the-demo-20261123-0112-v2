#!/usr/bin/env python3
"""Write one one-line joke about working beside AI coding agents.

Deterministic: a fixed string, no randomness, no network, no time.
Writes to /output/entry.txt (created if missing).
"""
import os

JOKE = (
    "Halfway through the demo, my coding agent froze, turned to the audience, "
    "and asked if anyone knew how to fix the code it had just written."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
