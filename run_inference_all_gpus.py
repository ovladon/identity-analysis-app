#!/usr/bin/env python3
"""
run_inference_all_gpus.py

A production‐ready, multi‐GPU inference script to process all Gutenberg autobiographies
using all available A100 GPUs. Wraps your model in DataParallel and writes JSON + PNG outputs.

Prerequisites:
  • data/gutenberg_autobiography_ids.csv  exists
  • data/paragraphs/<id>_<safe_title>.txt  for each book
  • Your existing scoring and plotting functions (replace stubs below)

Usage:
  python run_inference_all_gpus.py
"""

import os
import csv
import glob
import json
from pathlib import Path
from typing import List, Dict

import torch
from torch.nn.functional import normalize
from torch.nn import DataParallel
from transformers import AutoTokenizer, AutoModel

# === Replace these stubs with your actual scoring + plotting logic ===
def score_paragraphs(model, tokenizer, texts: List[str], device: torch.device) -> List[Dict[str, float]]:
    # Example placeholder: return zeroed scores for 19 constructs
    dummy = {f"construct_{i}": 0.0 for i in range(19)}
    return [dummy.copy() for _ in texts]

def plot_sunburst(scores: List[Dict[str, float]], title: str, out_path: Path):
    # Placeholder: replace with your src/visualization.py sunburst‐plot code
    pass
# =======================================================================

def main():
    # 1. Detect GPUs
    num_gpus = torch.cuda.device_count()
    assert num_gpus > 0, "No GPUs detected; ensure your CUDA environment is set up."
    print(f"Detected {num_gpus} GPU(s): {[torch.cuda.get_device_name(i) for i in range(num_gpus)]}")

    # 2. Load tokenizer & base model, wrap in DataParallel
    device = torch.device("cuda:0")
    model_name = "bert-base-uncased"  # <-- replace with your model path/name
    print(f"Loading model '{model_name}'...")
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    base_model = AutoModel.from_pretrained(model_name)

    if num_gpus > 1:
        model = DataParallel(base_model)
    else:
        model = base_model
    model.to(device)
    model.eval()

    # 3. Read metadata CSV
    meta_csv = Path("data/gutenberg_autobiography_ids.csv")
    assert meta_csv.exists(), f"{meta_csv} not found!"
    books = []
    with open(meta_csv, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            gid = row["gutenberg_id"]
            title = row["title"]
            safe_title = title.replace("/", "_").replace(" ", "_").replace(":", "_")
            authors = row["authors"]
            books.append((gid, safe_title, authors))
    print(f"Total books to process: {len(books)}")

    # 4. Process each book
    out_dir = Path("results/gutenberg_runs")
    out_dir.mkdir(parents=True, exist_ok=True)
    for gid, safe_title, authors in books:
        para_file = Path(f"data/paragraphs/{gid}_{safe_title}.txt")
        if not para_file.exists():
            print(f"  [Warning] Missing paragraphs for {gid}: {para_file}")
            continue
        print(f"Processing {gid}: {safe_title} …")

        raw = para_file.read_text(encoding="utf-8")
        paragraphs = [p.strip() for p in raw.split("\n\n") if p.strip()]
        if not paragraphs:
            print(f"  [Warning] No paragraphs in {para_file}. Skipping.")
            continue

        batch_size = 128
        all_scores = []
        for i in range(0, len(paragraphs), batch_size):
            batch = paragraphs[i : i + batch_size]
            with torch.no_grad():
                scores = score_paragraphs(model, tokenizer, batch, device)
            all_scores.extend(scores)
            torch.cuda.empty_cache()

        # 5. Save JSON
        json_path = out_dir / f"{gid}_results.json"
        payload = {
            "gutenberg_id": gid,
            "title": safe_title,
            "authors": authors,
            "paragraph_scores": all_scores,
        }
        with open(json_path, "w", encoding="utf-8") as jf:
            json.dump(payload, jf, indent=2)
        print(f"  ✓ JSON → {json_path}")

        # 6. Save sunburst PNG
        png_path = out_dir / f"{gid}_sunburst.png"
        plot_sunburst(all_scores, title=safe_title, out_path=png_path)
        print(f"  ✓ PNG → {png_path}")

    print("All books processed.")

if __name__ == "__main__":
    main()
