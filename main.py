#!/usr/bin/env python3
"""One Word for Your Wi-Fi - entry program.

Writes the single word that best describes my Wi-Fi to /output/entry.txt.
The word is the whole entry: one word, UTF-8, 1-20 characters.
"""
import os
from pathlib import Path

WORD = "Buffering"

def main() -> None:
    out_dir = Path(os.environ.get("ENTRY_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(WORD, encoding="utf-8")

if __name__ == "__main__":
    main()
