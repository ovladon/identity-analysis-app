# constructs/actual_self.py
# ---------------------------------------------------------------------------
# Self-Concept – Actual Self (how person currently sees themselves)
# ---------------------------------------------------------------------------
from .keyword_and_model_construct import KeywordAndModelConstruct

KEYWORDS = [
    "I am ", "I'm ", "I am a ", "my self-image", "the real me",
    "who I am", "currently", "at present", "as I am", "myself",
    "in reality", "truth is", "fact is", "today I", "right now",
    "see myself", "consider myself", "describe myself", "I feel",
    "I think I am", "I view myself", "my current", "my present",
    "as of now", "in fact", "identify as", "define myself"
]

PHRASES = [
    "this is who I am", "in real life", "in reality I",
    "my real self", "actual self", "present self"
]


class ActualSelf(KeywordAndModelConstruct):
    def __init__(self, tokenizer, model):
        super().__init__(
            "ActualSelf",
            KEYWORDS, PHRASES,
            ["describes present self", "no present self"],
            tokenizer, model
        )
        self.words = set(KEYWORDS + PHRASES)

    def analyze_text(self, text):
        t  = text.lower()
        kw = sum(1 for w in self.words if w in t) / len(self.words)
        zs = self._zs_prob(t, ["describes present self",
                               "no present self description"])
        return {self.name: {"CRS": (0.5 * kw + 0.5 * zs) * 100}}

