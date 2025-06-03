#!/usr/bin/env python3
"""
evaluate_gutenberg.py

Aggregates all JSON outputs from results/gutenberg_runs/ into a single CSV summary.
For each book:
  - Reads <gutenberg_id>_results.json (which contains per-paragraph scores).
  - Computes average and peak (max) of each construct across paragraphs.
  - Merges with metadata (title, authors) from data/gutenberg_autobiography_ids.csv.
  - Writes evaluation_summary.csv in results/gutenberg_runs/.

Usage:
  python src/evaluation/evaluate_gutenberg.py \
    --results_dir results/gutenberg_runs \
    --metadata_csv data/gutenberg_autobiography_ids.csv
"""

import os
import csv
import glob
import json
import argparse
from pathlib import Path
from collections import defaultdict

import pandas as pd

def parse_args():
    parser = argparse.ArgumentParser(
        description="Aggregate paragraph-level JSONs into a summary CSV."
    )
    parser.add_argument(
        "--results_dir",
        type=str,
        required=True,
        help="Directory containing <gid>_results.json files."
    )
    parser.add_argument(
        "--metadata_csv",
        type=str,
        required=True,
        help="CSV file with columns [gutenberg_id, title, authors]."
    )
    return parser.parse_args()

def load_metadata(metadata_csv: str):
    """Reads metadata CSV into a DataFrame."""
    if not os.path.exists(metadata_csv):
        raise FileNotFoundError(f"Metadata file not found: {metadata_csv}")
    meta_df = pd.read_csv(metadata_csv, dtype={"gutenberg_id": str})
    return meta_df

def aggregate_json(json_path: str):
    """
    Given a single <gid>_results.json, compute:
      - avg_{construct} (mean over paragraphs)
      - peak_{construct} (max over paragraphs)
    Returns a dict: {"avg_agency": 0.23, "peak_agency": 0.78, …}
    """
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    para_scores = data.get("paragraph_scores", [])
    if not para_scores:
        return {}
    # Collect per-construct lists
    scores_by_construct = defaultdict(list)
    for para in para_scores:
        for k, v in para.items():
            scores_by_construct[k].append(v)
    summary = {}
    for construct, vals in scores_by_construct.items():
        summary[f"avg_{construct}"] = sum(vals) / len(vals)
        summary[f"peak_{construct}"] = max(vals)
    return summary

def main():
    args = parse_args()
    results_dir = Path(args.results_dir)
    metadata_csv = args.metadata_csv

    # 1. Load metadata
    meta_df = load_metadata(metadata_csv)
    meta_df["gutenberg_id"] = meta_df["gutenberg_id"].astype(str)

    # 2. Initialize a list of summary rows
    summary_rows = []

    # 3. Iterate over all *_results.json in results_dir
    json_files = sorted(glob.glob(str(results_dir / "*_results.json")))
    if not json_files:
        raise FileNotFoundError(f"No JSON files found in {results_dir}")

    for json_file in json_files:
        fname = os.path.basename(json_file)
        gid = fname.split("_")[0]  # assumes filename "<gid>_results.json"
        # 3a. Load and aggregate
        agg = aggregate_json(json_file)
        if not agg:
            print(f"[Warning] No paragraph_scores in {json_file}, skipping.")
            continue

        # 3b. Merge with metadata row for this gid
        meta_row = meta_df[meta_df["gutenberg_id"] == gid]
        if meta_row.empty:
            print(f"[Warning] Metadata missing for {gid}, skipping.")
            continue
        title = meta_row.iloc[0]["title"]
        authors = meta_row.iloc[0]["authors"]

        row = {"gutenberg_id": gid, "title": title, "authors": authors}
        row.update(agg)
        summary_rows.append(row)

    if not summary_rows:
        print("No valid data to write. Exiting.")
        return

    # 4. Build DataFrame and write CSV
    summary_df = pd.DataFrame(summary_rows)
    # Sort by integer gutenberg_id if numeric, else lexicographically
    try:
        summary_df["gutenberg_id_int"] = summary_df["gutenberg_id"].astype(int)
        summary_df = summary_df.sort_values("gutenberg_id_int")
        summary_df = summary_df.drop(columns=["gutenberg_id_int"])
    except ValueError:
        summary_df = summary_df.sort_values("gutenberg_id")

    # 5. Output path
    out_csv = results_dir / "evaluation_summary.csv"
    summary_df.to_csv(out_csv, index=False, encoding="utf-8")
    print(f"✓ Wrote evaluation summary → {out_csv}")

if __name__ == "__main__":
    main()
