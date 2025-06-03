"""
Shared base class for all construct detectors.

Adds:
  • _zs_prob()   – safe wrapper for BART zero-shot pipeline
  • _suggest_terms() – logs unseen high-probability n-grams for human review
"""

from model_loader import model_loader, zero_shot_pipe
from typing import List, Dict
import pathlib, re

class KeywordAndModelConstruct:
    SUGGEST_DIR = pathlib.Path("lexicon_suggestions")

    def __init__(
        self,
        name: str,
        keywords: List[str],
        phrases: List[str],
        labels: List[str],
        tokenizer,
        model,
    ):
        self.name      = name
        self.keywords  = keywords
        self.phrases   = phrases
        self.labels    = labels
        self.tokenizer = tokenizer
        self.model     = model
        self.zero_shot = zero_shot_pipe          # shared cached BART

        # word set for fast membership tests
        self.words = set(map(str.lower, keywords + phrases))

        # ensure suggestion dir exists
        self.SUGGEST_DIR.mkdir(exist_ok=True)

    # --------------------------------------------------------------------- #
    def _zs_prob(self, text: str, labels: List[str]) -> float:
        """Return P(labels[0] | text) or 0.0 on failure."""
        try:
            res = self.zero_shot(text, labels)
            return res["scores"][0]
        except Exception:
            return 0.0

    # --------------------------------------------------------------------- #
    def _suggest_terms(self, text: str, prob: float, kw_hits: int) -> None:
        """
        If BART says prob>0.8 but we had no keyword hits,
        log noun/verb/adjective n-grams for later lexicon review.
        """
        if prob < 0.8 or kw_hits > 0:
            return
        # very naive n-gram finder: words 4-12 chars that aren't in lexicon
        for w in re.findall(r"\b[a-z]{4,12}\b", text.lower()):
            if w not in self.words:
                with open(self.SUGGEST_DIR / f"{self.name}.txt", "a") as fp:
                    fp.write(w + "\n")

