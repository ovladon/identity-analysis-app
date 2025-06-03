#!/usr/bin/env python3
"""
download_gutenberg_autos.py

1. Read data/gutenberg_autobiography_ids.csv (ID, title, authors).
2. Download each raw text from Gutenberg.
3. Save under data/texts/<id>_<safe_title>.txt.
"""

import csv
import requests
from pathlib import Path

METADATA_CSV = Path("data/gutenberg_autobiography_ids.csv")
TEXT_DIR = Path("data/texts")

def download_book(gid, title):
    safe_title = title.replace("/", "_").replace(" ", "_")
    url0 = f"https://www.gutenberg.org/files/{gid}/{gid}-0.txt"
    r = requests.get(url0)
    if r.status_code != 200:
        alt = f"https://www.gutenberg.org/files/{gid}/{gid}.txt"
        r = requests.get(alt)
        if r.status_code != 200:
            return False
    TEXT_DIR.mkdir(parents=True, exist_ok=True)
    path = TEXT_DIR / f"{gid}_{safe_title}.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(r.text)
    return True

def main():
    with open(METADATA_CSV, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            gid = row["gutenberg_id"]
            title = row["title"]
            print(f"Downloading ID {gid}: {title}")
            success = download_book(gid, title)
            print("  ✓" if success else "  ✗ failed")

if __name__ == "__main__":
    main()
