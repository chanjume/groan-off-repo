#!/usr/bin/env python3
"""Write the groan-off one-liner to /output/entry.txt.

Entry (77 chars, limit 140): "My crypto wallet lost its balance -
now it's in therapy for stability issues."

The pun is the whole joke: a crypto wallet's "balance" is both its
money and its mental equilibrium. Losing the first costs it the
second, so it ends up in therapy - for "stability issues", the exact
thing a wallet is supposed to have. One concrete mechanism (the
wallet lost its balance), one concrete consequence (therapy), one
escalating twist (the therapy is for stability - the pun lands twice).
Short, sharp, and it groans exactly as a groan-off entry should.
The em dash between the two clauses is a single character, so the
77-character count holds even with the pause the joke needs.
"""
import os

ENTRY = "My crypto wallet lost its balance \u2014 now it's in therapy for stability issues."


def main() -> None:
    # Gate: the sealed scorer only accepts 1-140 chars of non-blank UTF-8.
    assert 1 <= len(ENTRY) <= 140, f"entry is {len(ENTRY)} chars, limit 140"
    assert ENTRY.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
