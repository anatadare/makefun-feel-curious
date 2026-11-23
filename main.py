#!/usr/bin/env python3
"""The Drawer Dated Next Thursday.

Writes one short mystery to /output/entry.txt. The text is meant to make
the reader curious: a drawer locked for sixty years, a key found only
yesterday, and inside it a note in the narrator's own handwriting,
dated next Thursday.

Python 3.13 standard library only. No network access.
"""

import os

OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")

TEXT = (
    "My grandmother kept one drawer locked for sixty years and never told "
    "anyone why. Yesterday I found the key. Inside was a single note, "
    "written in my handwriting, dated next Thursday."
)


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
