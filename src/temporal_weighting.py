"""
Temporal weighting of CRS scores by inferred age of events.

Now robust to arbitrarily large inputs:
  • nlp_small.max_length raised to 2.5 M
  • texts > CHUNK_LIMIT are processed in slices of ≤100 k characters.
"""

from __future__ import annotations
import re, spacy, itertools
from typing import Dict, List

nlp_small = spacy.load("en_core_web_sm")
nlp_small.max_length = 2_500_000          # raise spaCy limit

CHUNK_LIMIT = 100_000                     # chunk size for streaming

AGE_TABLE: List[tuple[int, int, List[str]]] = [
    (0,   2,  ['TrustVsMistrust']),
    (2,   4,  ['AutonomyVsShameDoubt']),
    (4,   6,  ['InitiativeVsGuilt']),
    (6,  12,  ['IndustryVsInferiority']),
    (12, 18,  ['IdentityDiffusion','IdentityForeclosure',
               'IdentityMoratorium','IdentityAchievement',
               'IdentityVsRoleConfusion']),
    (18, 40,  ['IntimacyVsIsolation']),
    (40, 65,  ['GenerativityVsStagnation']),
    (65, 150, ['EgoIntegrityVsDespair'])
]
AGE_BAND = {c: (lo, hi) for lo, hi, names in AGE_TABLE for c in names}

_age_rgx = re.compile(
    r'(?:when|at|aged)?\s*(?:I\s*)?(?:was|am|age[d]?|turned)?\s*'
    r'(\d{1,2})\s*(?:years|yrs|y/o|yo)?', re.I
)

def _extract_age(sent: str) -> int | None:
    m = _age_rgx.search(sent)
    return int(m.group(1)) if m and 0 < int(m.group(1)) < 120 else None

def _band_match(age: int, construct: str) -> bool:
    lo, hi = AGE_BAND.get(construct, (None, None))
    return lo is not None and lo <= age < hi

def _sent_stream(text: str):
    """Yield spaCy sentence objects in ≤100k-char chunks."""
    for i in range(0, len(text), CHUNK_LIMIT):
        doc = nlp_small(text[i:i+CHUNK_LIMIT])
        for sent in doc.sents:
            yield sent

def weight_crs_by_age(text: str, cs: Dict[str, Dict]) -> Dict[str, Dict]:
    # collect constructs that receive an age-appropriate hit
    constructs_in_band = set()
    for sent in _sent_stream(text):
        age = _extract_age(sent.text)
        if age is None: continue
        for c in AGE_BAND:
            if _band_match(age, c):
                constructs_in_band.add(c)

    # rewrite CRS
    for c, d in cs.items():
        raw = d['CRS']
        weight = 1.0 if c in constructs_in_band else 0.7   # keep 0.7 or 0.5 as you prefer
        d['CRS_raw'] = raw
        d['CRS'] = raw * weight
        d['age_weight'] = weight
    return cs

