#!/usr/bin/env python3
"""Count words in a markdown or plain-text doc, ignoring markdown syntax.

Usage:
    python3 wordcount.py before.md after.md   # prints both counts and the change
    python3 wordcount.py doc.md               # prints one count
    cat doc.md | python3 wordcount.py         # reads stdin
"""
import re
import sys


def count(text: str) -> int:
    text = re.sub(r"```.*?```", " ", text, flags=re.S)        # code blocks
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)       # links: keep the label
    text = re.sub(r"^\s*\|?\s*:?-{3,}.*$", " ", text, flags=re.M)  # table separator rows
    text = re.sub(r"[|#*_`>]+", " ", text)                     # remaining markdown symbols
    text = re.sub(r"^\s*(?:[-+]|\d+\.)\s+", " ", text, flags=re.M)  # list markers
    return len(re.findall(r"[^\W_][\w'’.,%/×÷+≥≤<>-]*", text))


def main(argv):
    if not argv:
        print(count(sys.stdin.read()))
        return
    counts = [count(open(p, encoding="utf-8").read()) for p in argv]
    if len(counts) == 2:
        a, b = counts
        pct = round((b - a) / a * 100) if a else 0
        print(f"{a:,} → {b:,} ({pct:+d}%)".replace("+-", "−").replace("-", "−"))
    else:
        for p, c in zip(argv, counts):
            print(f"{c:,}\t{p}")


if __name__ == "__main__":
    main(sys.argv[1:])
