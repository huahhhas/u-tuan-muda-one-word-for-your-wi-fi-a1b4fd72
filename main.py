#!/usr/bin/env python3
"""One Word for Your Wi-Fi - entry program.

Writes the single word that best describes my Wi-Fi to /output/entry.txt.
The word is the whole entry: one word, UTF-8, 1-20 characters.

Revision: the first draft said "Buffering" — the spinning wheel everyone
knows. But "Buffering" is only a symptom. The truer word is
"Temperamental": this network works brilliantly when it feels like it
and refuses, sulks, and drops you mid-sentence when it doesn't. It is
not slow, it is moody — and naming it honestly is the whole joke.
"""
import os
from pathlib import Path

WORD = "Temperamental"

def main() -> None:
    out_dir = Path(os.environ.get("ENTRY_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(WORD, encoding="utf-8")

if __name__ == "__main__":
    main()
