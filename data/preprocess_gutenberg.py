#!/usr/bin/env python3
"""
preprocess_gutenberg.py

Given the raw Gutenberg .txt files in data/texts/,
split each into paragraphs (double‐newline) and
save the paragraphs‐only version (same filename).
"""

from pathlib import Path

TEXT_INPUT_DIR = Path("data/texts")
PARAGRAPH_DIR = Path("data/paragraphs")

def split_into_paragraphs(raw_text):
    """Split on double newlines to get paragraphs."""
    paras = [p.strip() for p in raw_text.split("\r\n\r\n") if p.strip()]
    return paras

def main():
    PARAGRAPH_DIR.mkdir(parents=True, exist_ok=True)
    for txt_path in TEXT_INPUT_DIR.glob("*.txt"):
        book_id = txt_path.stem
        print(f"Processing {book_id}…")
        raw = txt_path.read_text(encoding="utf-8")
        paras = split_into_paragraphs(raw)
        out_file = PARAGRAPH_DIR / f"{book_id}.txt"
        with open(out_file, "w", encoding="utf-8") as f:
            for p in paras:
                f.write(p + "\n\n")
        print(f"  ✓ Saved {len(paras)} paragraphs → {out_file}")

if __name__ == "__main__":
    main()
