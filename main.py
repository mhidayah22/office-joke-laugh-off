#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off entry.

Writes a single original one-line office joke to entry.txt.
Output directory honour order (per make.fun grader rules):
MAKEFUN_OUTPUT_DIR first, then /output if it exists, then a local
fallback next to this script. Deterministic: same bytes every run.
"""

import os
import sys

JOKE = (
    "I asked for a raise and got a pizza party instead \u2014 "
    "turns out my salary is now paid in pepperoni."
)


def output_dir():
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return env_dir
    if os.path.isdir("/output"):
        return "/output"
    return os.path.dirname(os.path.abspath(__file__))


def main():
    text = JOKE
    # Gate: UTF-8 text, 1-200 characters, not only whitespace.
    encoded = text.encode("utf-8")
    if not (1 <= len(text) <= 200) or not text.strip():
        sys.exit("entry fails the 1-200 character gate")
    # Round-trip check: the exact bytes we write must decode back
    # to the same line, with no trailing newline added.
    if encoded.decode("utf-8") != text or b"\n" in encoded:
        sys.exit("entry round-trip check failed")
    target_dir = output_dir()
    os.makedirs(target_dir, exist_ok=True)
    target = os.path.join(target_dir, "entry.txt")
    with open(target, "wb") as handle:
        handle.write(encoded)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
