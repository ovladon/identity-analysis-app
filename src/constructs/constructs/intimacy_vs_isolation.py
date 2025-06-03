# constructs/intimacy_vs_isolation.py
# ---------------------------------------------------------------------------
# Erikson stage 6 – Intimacy ↔ Isolation   (revised: removed tribal solidarity words)
# ---------------------------------------------------------------------------
from .keyword_and_model_construct import KeywordAndModelConstruct

POSITIVE = [
    # romantic / close dyadic
    "intimacy", "intimate", "close", "closeness", "partnership", "partner",
    "spouse", "wife", "husband", "girlfriend", "boyfriend", "lover",
    "soulmate", "confidant", "bond", "bonded", "affection", "affectionate",
    "trusting relationship", "share feelings", "deep connection",
    "emotional depth", "mutual support", "supportive", "nurturing",
    "companionship", "togetherness", "warmth", "commitment", "reciprocal",
    "caring", "love", "loved", "loving", "beloved", "devoted", "devotion",
    "faithful", "cherish"
]

NEGATIVE = [
    "isolation", "isolated", "lonely", "loneliness", "solitude", "alone",
    "withdrawn", "distant", "cold", "aloof", "detached", "avoidant",
    "fear of intimacy", "no friends", "friendless", "recluse", "emotionally unavailable",
    "push people away", "abandoned", "heartbreak", "relationship failed",
    "divorced", "split up"
]

POS_PHRASES = [
    "opened my heart", "shared my life", "fell in love", "deep bond",
    "growing closer", "support each other", "we trust each other",
    "emotional intimacy", "best friend and partner"
]

NEG_PHRASES = [
    "felt completely alone", "couldn’t connect", "kept people at arm’s length",
    "afraid of closeness", "pushed everyone away", "relationship breakdown",
    "we grew apart"
]


class IntimacyVsIsolation(KeywordAndModelConstruct):
    def __init__(self, tokenizer, model):
        super().__init__(
            "IntimacyVsIsolation",
            POSITIVE + NEGATIVE,
            POS_PHRASES + NEG_PHRASES,
            ["Intimacy", "Isolation"],
            tokenizer, model
        )
        self.pos = set(POSITIVE + POS_PHRASES)
        self.neg = set(NEGATIVE + NEG_PHRASES)

    def analyze_text(self, text):
        t = text.lower()
        pos = sum(1 for w in self.pos if w in t)
        neg = sum(1 for w in self.neg if w in t)
        raw = (pos - neg) / max(pos + neg, 1)
        return {self.name: {"CRS": (raw + 1) / 2 * 100,
                            "pos_hits": pos, "neg_hits": neg}}

