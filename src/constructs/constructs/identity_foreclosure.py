# constructs/identity_foreclosure.py
# ---------------------------------------------------------------------------
# Marcia status – Identity Foreclosure
# ---------------------------------------------------------------------------
from .keyword_and_model_construct import KeywordAndModelConstruct

KEYWORDS = [
    "foreclosure", "identity foreclosure", "never questioned", "unquestioned",
    "handed-down values", "family expectations", "pre-set path", "pre set path",
    "follow footsteps", "following footsteps", "took it for granted",
    "accepted without question", "inherited role", "duty-bound",
    "decided for me", "decided by parents", "conventional", "traditional",
    "conform", "conformity", "obliged", "obligation", "expected to be",
    "was told", "obeyed", "obedient", "surrendered choice", "no exploration"
]

PHRASES = [
    "I always knew I would", "it was assumed", "I had no choice",
    "what my family expected", "continued the family tradition",
    "took over the family business"
]


class IdentityForeclosure(KeywordAndModelConstruct):
    def __init__(self, tokenizer, model):
        super().__init__(
            "IdentityForeclosure",
            KEYWORDS, PHRASES,
            ["foreclosure", "open exploration"],
            tokenizer, model
        )
        self.words=set(KEYWORDS+PHRASES)

    def analyze_text(self, text):
        t  = text.lower()
        kw = sum(1 for w in self.words if w in t) / len(self.words)
        zs = self._zs_prob(t, ["identity foreclosed", "identity open"])
        return {self.name: {"CRS": (0.5 * kw + 0.5 * zs) * 100}}

