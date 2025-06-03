#!/usr/bin/env python3
"""
download_gutenberg.py (topic‐based)

1. Query Gutendex for all books tagged under “Autobiography” in English.
2. Save the CSV of IDs/titles/authors.
3. Download each raw .txt from Gutenberg.
"""

import requests
import csv
from pathlib import Path

API_URL = "https://gutendex.com/books?topic=Autobiography&languages=en"
CSV_OUT = Path("data/gutenberg_metadata.csv")
TEXT_DIR = Path("data/texts")

def fetch_autobiographies_once():
    resp = requests.get(API_URL)
    resp.raise_for_status()
    data = resp.json()
    # Gutendex “topic” search may still paginate if >32 results
    books = data.get("results", [])
    next_page = data.get("next")
    while next_page:
        resp = requests.get(next_page)
        resp.raise_for_status()
        data = resp.json()
        books.extend(data.get("results", []))
        next_page = data.get("next")
    return books

def save_csv(books):
    with open(CSV_OUT, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["gutenberg_id", "title", "authors"])
        for book in books:
            gid = book["id"]
            title = book["title"]
            authors = ";".join([a["name"] for a in book.get("authors", [])])
            writer.writerow([gid, title, authors])

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
    print("Fetching all books tagged 'Autobiography' (English) …")
    books = fetch_autobiographies_once()
    print(f"  • Retrieved {len(books)} entries.")
    save_csv(books)
    print(f"  • Saved metadata to {CSV_OUT}")
    print("Downloading raw texts:")
    for book in books:
        gid = book["id"]
        title = book["title"]
        print(f"  - {gid}: {title}")
        success = download_book(gid, title)
        print("    ✓" if success else "    ✗")
    print("Done.")
if __name__ == "__main__":
    main()
