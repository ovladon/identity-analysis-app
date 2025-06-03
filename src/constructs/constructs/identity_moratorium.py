# constructs/identity_moratorium.py
# ---------------------------------------------------------------------------
# Marcia status – Identity Moratorium (high exploration, low commitment)
# ---------------------------------------------------------------------------
from .keyword_and_model_construct import KeywordAndModelConstruct

KEYWORDS = [
    "moratorium", "identity moratorium", "searching", "seeking",
    "exploring options", "experimenting", "trying out roles",
    "still deciding", "in flux", "undecided", "tentative", "questioning",
    "open-ended", "keeping options open", "no final choice", "continuing search",
    "unresolved", "identity crisis", "in crisis", "looking for answers",
    "soul searching", "probing", "hung in balance", "on hold", "delay commitment"
]

PHRASES = [
    "I haven't settled yet", "I'm still figuring it out", "not ready to commit",
    "shopping around", "testing the waters", "trying different paths"
]


class IdentityMoratorium(KeywordAndModelConstruct):
    def __init__(self, tokenizer, model):
        super().__init__(
            "IdentityMoratorium",
            KEYWORDS, PHRASES,
            ["identity search", "identity commitment"],
            tokenizer, model
        )
        self.words=set(KEYWORDS+PHRASES)

    def analyze_text(self, text):
        t  = text.lower()
        kw = sum(1 for w in self.words if w in t) / len(self.words)
        zs = self._zs_prob(t, ["in identity moratorium", "identity settled"])
        return {self.name: {"CRS": (0.5 * kw + 0.5 * zs) * 100}}

