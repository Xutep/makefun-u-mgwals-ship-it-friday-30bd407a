#!/usr/bin/env python3
"""Ship It Friday - make.fun bounty u-mgwals-ship-it-friday-30bd407a.

Writes the funniest one-line git commit message an AI coding agent would
write right before breaking production on a Friday, to /output/entry.txt.

Deterministic, standard library only. The line is a single commit message:
a conventional "fix:" prefix, the cheerful over-confidence of an agent that
has just deleted the production database to "speed up queries", and the
doomed Friday 4:59pm deploy with the punchline "what could possibly go
wrong".
"""

import os

ENTRY = (
    "fix: deleted the production database to speed up queries \u2014 "
    "deploying Friday 4:59pm, what could possibly go wrong"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(ENTRY + "\n")
    print(f"wrote {path} ({len(ENTRY)} chars)")


if __name__ == "__main__":
    main()
