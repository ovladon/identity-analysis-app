# constructs/meaning_making.py
# ---------------------------------------------------------------------------
# Narrative Identity – Meaning Making / Autobiographical Reasoning
# Sources: Habermas & Bluck 2000; McLean & Pratt 2006.
# ---------------------------------------------------------------------------
from .keyword_and_model_construct import KeywordAndModelConstruct

KEYWORDS = [
    "meaning", "meaningful", "made meaning", "found meaning", "gave meaning",
    "understand", "understood", "understanding", "lesson", "lessons",
    "learned", "learning", "insight", "insights", "insightful", "realise",
    "realised", "realization", "realisation", "taught me", "teaches", "taught",
    "wisdom", "grew", "growth", "perspective", "reflect", "reflection",
    "reflected", "looking back", "takeaway", "moral", "significance",
    "value in", "purpose", "purposeful", "sense-making", "sense making",
    "interpret", "interpreted", "interpreting", "framework", "lesson from",
    "what I took", "bigger picture", "shaped me", "shaped my", "changed me",
    "because of that I", "it showed me", "I realised that"
]

PHRASES = [
    "I learned that", "this taught me", "made me realise",
    "what I took from that", "helped me grow", "gave me a new perspective",
    "the moral is", "I came to understand", "I found meaning in"
]


class MeaningMaking(KeywordAndModelConstruct):
    def __init__(self, tokenizer, model):
        super().__init__(
            "MeaningMaking",
            KEYWORDS, PHRASES,
            ["meaning making present","no meaning making"],
            tokenizer, model
        )
        self.words=set(KEYWORDS+PHRASES)

    def analyze_text(self, text):
        t  = text.lower()
        kw = sum(1 for w in self.words if w in t) / len(self.words)
        zs = self._zs_prob(t, ["explicit reflection", "no reflection"])
        return {self.name: {"CRS": (0.4 * kw + 0.6 * zs) * 100}}

