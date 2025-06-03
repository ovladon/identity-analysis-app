"""
preprocessing.py
• Cleans Unicode cruft
• Lemmatizes with spaCy en_core_web_lg
Handles arbitrarily large files by streaming in 100 k-char chunks
if len(text) > CHUNK_LIMIT.
"""

import unicodedata, spacy, itertools

# 1.  Load models
nlp_lg = spacy.load("en_core_web_lg")
nlp_lg.max_length = 2_500_000          # <-- Fix A: raise hard limit

# 2.  parameters
CHUNK_LIMIT = 100_000                  # 100k char safe size

def _clean(t: str) -> str:
    return unicodedata.normalize("NFKD", t).replace("\u200b", "")

def _lemmatise_chunk(chunk: str) -> str:
    return " ".join(tok.lemma_ for tok in nlp_lg(chunk))

def _chunks(text: str, size: int):
    """Yield non-overlapping text slices ≤ size."""
    for i in range(0, len(text), size):
        yield text[i:i+size]

def preprocess_text(text: str) -> str:
    txt = _clean(text)
    if len(txt) <= CHUNK_LIMIT:                # small file
        return _lemmatise_chunk(txt)

    # Fix B: stream large docs
    lemmas = (_lemmatise_chunk(chunk) for chunk in _chunks(txt, CHUNK_LIMIT))
    return " ".join(lemmas)

