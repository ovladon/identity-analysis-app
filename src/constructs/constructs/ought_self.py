# constructs/ought_self.py
# ---------------------------------------------------------------------------
# Self-Concept – Ought Self (duties & obligations)
# ---------------------------------------------------------------------------
from .keyword_and_model_construct import KeywordAndModelConstruct

KEYWORDS = [
    "should ", "shouldn't", "must ", "mustn't", "have to", "need to",
    "ought to", "supposed to", "expected to", "duty", "duty-bound",
    "obligation", "obliged", "responsibility", "responsible for",
    "required to", "requirement", "mandatory", "moral duty", "ethical duty",
    "feel compelled", "I'm meant to", "society expects", "parents expect",
    "bound to", "burden", "must fulfill", "must fulfil", "live up to",
    "live up to", "must obey", "obedient", "compliance"
]

PHRASES = [
    "it is my duty", "I am supposed to", "I feel obligated",
    "society expects me to", "I should have", "I must", "I have to",
    "I ought to"
]


class OughtSelf(KeywordAndModelConstruct):
    def __init__(self, tokenizer, model):
        super().__init__(
            "OughtSelf",
            KEYWORDS, PHRASES,
            ["sense of obligation", "no obligation language"],
            tokenizer, model
        )
        self.words = set(KEYWORDS + PHRASES)

    def analyze_text(self, text):
        t  = text.lower()
        kw = sum(1 for w in self.words if w in t) / len(self.words)
        zs = self._zs_prob(t, ["sense of obligation",
                               "no sense of obligation"])
        return {self.name: {"CRS": (0.5 * kw + 0.5 * zs) * 100}}

