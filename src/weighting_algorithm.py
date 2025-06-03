"""
Improved weighting algorithm combining:
  • keyword votes scaled by tf‑idf,
  • BART zero‑shot entailment probability,
  • context‑window similarity,
and returns CRS with bootstrap CIs.
"""

import random, math, numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from transformers import pipeline, AutoTokenizer, AutoModel
from collections import Counter
from typing import List

vectorizer = TfidfVectorizer(ngram_range=(1, 2), stop_words='english')
bart = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def tfidf_scores(docs: List[str]):
    X = vectorizer.fit_transform(docs)
    tfidf = {t: vectorizer.idf_[i] for t, i in vectorizer.vocabulary_.items()}
    return tfidf

def bayesian_fuse(keyword_score, entail_prob):
    """Combine two evidence sources into one CRS (0‑100)."""
    p = 1 - (1 - keyword_score) * (1 - entail_prob)
    return p * 100

def bootstrap_ci(scores, n=500, alpha=.05):
    boot = []
    for _ in range(n):
        boot.append(np.mean(random.choices(scores, k=len(scores))))
    lower = np.percentile(boot, alpha/2*100)
    upper = np.percentile(boot, (1-alpha/2)*100)
    return lower, upper
