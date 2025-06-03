"""
model_loader.py
Central access to:
  • sentence-embedding model (SimCSE)
  • tokenizer
  • shared zero-shot classifier (facebook/bart-large-mnli)

After import this module exposes:
    model_loader      – singleton instance of ModelLoader
    zero_shot_pipe    – cached zero-shot pipeline
"""

from functools import lru_cache
from transformers import pipeline, AutoTokenizer, AutoModel

_ZS_MODEL  = "facebook/bart-large-mnli"
_EMB_MODEL = "princeton-nlp/sup-simcse-roberta-base"   # use *-large if RAM allows


@lru_cache(maxsize=1)
def _build_zero_shot():
    """Heavyweight BART-MNLI loaded once per process."""
    return pipeline("zero-shot-classification", model=_ZS_MODEL)


@lru_cache(maxsize=1)
def _build_embedder():
    tok = AutoTokenizer.from_pretrained(_EMB_MODEL)
    mod = AutoModel.from_pretrained(_EMB_MODEL)
    return tok, mod


class ModelLoader:
    """Legacy wrapper so existing detectors need no change."""

    def __init__(self):
        self._tok, self._mod = None, None
        # instantiate once so AttributeError never happens
        self.zero_shot_pipe = _build_zero_shot()

    def get_tokenizer(self):
        if self._tok is None:
            self._tok, self._mod = _build_embedder()
        return self._tok

    def get_model(self):
        if self._mod is None:
            self._tok, self._mod = _build_embedder()
        return self._mod

    # convenience identical to attribute
    def get_zero_shot(self):
        return self.zero_shot_pipe


# ─── Singleton objects others can import ------------------------------------
model_loader   = ModelLoader()
zero_shot_pipe = model_loader.zero_shot_pipe

