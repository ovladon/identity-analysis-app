# constructs/ideal_self.py
# ---------------------------------------------------------------------------
# Self-Concept – Ideal Self (hopes & aspirations)
# ---------------------------------------------------------------------------
from .keyword_and_model_construct import KeywordAndModelConstruct

KEYWORDS = [
    "wish to", "would like to", "hope to", "my dream", "dream of",
    "goal is", "goals are", "aspire", "aspiration", "one day",
    "someday", "in the future", "future self", "best self",
    "perfect self", "vision of myself", "ultimate self", "ambition",
    "I want to become", "I aim to", "I intend to", "strive for",
    "striving for", "my desire", "my longing", "I plan to", "I will be"
]

PHRASES = [
    "my dream is to", "my ideal self would", "someday I will",
    "I see myself becoming", "in an ideal world", "I picture myself"
]


class IdealSelf(KeywordAndModelConstruct):
    def __init__(self, tokenizer, model):
        super().__init__(
            "IdealSelf",
            KEYWORDS, PHRASES,
            ["speaks of hopes", "no hopes expressed"],
            tokenizer, model
        )
        self.words = set(KEYWORDS + PHRASES)

    def analyze_text(self, text):
        t  = text.lower()
        kw = sum(1 for w in self.words if w in t) / len(self.words)
        zs = self._zs_prob(t, ["speaks of hopes and aspirations",
                               "does not mention hopes"])
        return {self.name: {"CRS": (0.5 * kw + 0.5 * zs) * 100}}

