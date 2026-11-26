#!/usr/bin/env python3
"""Fortune Cookie Funnies for Engineers.

Writes the entry - one single-line fortune cookie message for a software
engineer - to /output/entry.txt. Standard library only, fully deterministic:
the same line is written on every run.

Final line (v3, after two in-session revisions): the v1 paradox about a
test that tests nothing was clever but cerebral; the v2 rule-of-three
about the error message won because its punch lands on the first read,
every engineer has met the confident but useless error message, and the
funniest phrase sits at the very end. Kept verbatim from v2.
"""

import os

ENTRY = (
    "Your error message will be clear, helpful, and completely "
    "unrelated to the problem."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 120, "entry must be 1-120 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY.isascii(), "entry must be plain ASCII"
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    directory = os.path.dirname(out_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
