#!/usr/bin/env python3
"""
find_all_autobiographies_gutenberg.py

1. Page through Gutenberg’s search results for "autobiography" (English).
2. Extract each eBook ID, title, and author from <li class="booklink"> entries.
3. Save results to data/gutenberg_autobiography_ids.csv.
"""

import requests
import csv
import time
from bs4 import BeautifulSoup
from pathlib import Path

BASE_SEARCH = "https://www.gutenberg.org/ebooks/search/?query=autobiography"
CSV_OUT = Path("data/gutenberg_autobiography_ids.csv")

def parse_search_page(html):
    """Extract (id, title, author) from one search result page."""
    soup = BeautifulSoup(html, "html.parser")
    books = []
    for li in soup.select("li.booklink"):
        a = li.find("a", href=True)
        href = a["href"]  # e.g. "/ebooks/148"
        try:
            gid = int(href.split("/")[2])
        except:
            continue
        title_tag = a.select_one("span.title")
        author_tag = a.select_one("span.subtitle")
        title = title_tag.text.strip() if title_tag else ""
        authors = author_tag.text.strip() if author_tag else ""
        books.append((gid, title, authors))
    return books

def fetch_all_books():
    all_books = []
    start_index = 0
    while True:
        url = f"{BASE_SEARCH}&start_index={start_index}"
        resp = requests.get(url)
        resp.raise_for_status()
        page_books = parse_search_page(resp.text)
        if not page_books:
            break
        all_books.extend(page_books)
        print(f"  • Fetched {len(page_books)} titles from start_index={start_index}")
        start_index += 25
        # Sleep to avoid hammering the server
        time.sleep(0.2)
    return all_books

def save_to_csv(entries, out_path=CSV_OUT):
    with open(out_path, "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["gutenberg_id", "title", "authors"])
        for gid, title, authors in entries:
            writer.writerow([gid, title, authors])

def main():
    print("Crawling Gutenberg search results for 'autobiography'…")
    books = fetch_all_books()
    print(f"Total autobiographies found: {len(books)}")
    save_to_csv(books)
    print(f"Saved metadata to {CSV_OUT!s}")

if __name__ == "__main__":
    main()
