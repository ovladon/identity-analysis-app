# constructs/identity_diffusion.py
# ---------------------------------------------------------------------------
# Marcia status – Identity Diffusion
# ---------------------------------------------------------------------------
from .keyword_and_model_construct import KeywordAndModelConstruct

KEYWORDS = [
    "identity diffusion", "diffuse identity", "drifting", "aimless",
    "no direction", "no plans", "apathetic", "apathy", "don’t care",
    "whatever", "nothing interests me", "no goals", "lost", "confused",
    "identity confusion", "uncertain", "can’t decide", "uncommitted",
    "lack of commitment", "no sense of self", "scattered", "fragmented",
    "avoidant", "diffuse-avoidant", "floating", "wander", "wandering",
    "dawdle", "stalling", "indecisive", "no idea", "I don’t know"
]

PHRASES = [
    "no idea what to do", "haven't thought about it", "life on hold",
    "nothing appeals to me", "can’t be bothered", "just drift along"
]


class IdentityDiffusion(KeywordAndModelConstruct):
    def __init__(self, tokenizer, model):
        super().__init__(
            "IdentityDiffusion",
            KEYWORDS, PHRASES,
            ["identity diffusion","identity committed"],
            tokenizer, model
        )
        self.words=set(KEYWORDS+PHRASES)

    def analyze_text(self, text):
        t  = text.lower()
        kw = sum(1 for w in self.words if w in t) / len(self.words)
        zs = self._zs_prob(t, ["identity diffuse", "identity stable"])
        return {self.name: {"CRS": (0.5 * kw + 0.5 * zs) * 100}}

