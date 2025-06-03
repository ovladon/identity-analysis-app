# constructs/communion.py
# ---------------------------------------------------------------------------
# Narrative Identity – Communion (love, friendship, dialogue)
# Sources: McAdams 2001; Wiggins 1991 interpersonal circumplex.
# ---------------------------------------------------------------------------
from .keyword_and_model_construct import KeywordAndModelConstruct

POSITIVE = [
    "communion", "connected", "connection", "bond", "bonded", "affection",
    "affectionate", "love", "loving", "loved", "cared for", "care",
    "caring", "nurture", "nurtured", "support", "supported", "supportive",
    "together", "togetherness", "friend", "friends", "friendship",
    "companionship", "companion", "team", "teammate", "partner", "partnership",
    "collaborate", "collaboration", "cooperate", "cooperation", "empathy",
    "empathic", "sympathy", "sympathetic", "shared", "share feelings",
    "share experiences", "unity", "belonging", "belong", "stood by",
    "side by side", "community", "communal", "mutual", "reciprocal",
    "trust", "trusted", "loyal", "loyalty", "warm", "warmth"
]

NEGATIVE = [
    "isolated", "isolation", "lonely", "loneliness", "detached", "detachment",
    "alienated", "alienation", "estranged", "estrangement", "alone",
    "abandoned", "rejected", "rejection", "ignored", "neglected",
    "misunderstood", "no friends", "friendless", "outsider", "excluded",
    "exclusion", "hostile", "hostility", "conflict", "betrayed", "betrayal",
    "distrust", "distrusted", "unloved", "cold", "indifferent", "selfish",
    "aloof", "distance", "distanced"
]

POS_PHRASES = [
    "felt close to", "opened up to", "shared my feelings", "we bonded",
    "stood together", "support each other", "deep connection", "showed empathy"
]

NEG_PHRASES = [
    "pushed me away", "grew apart", "felt excluded", "left me out",
    "nobody understood", "no one cared", "shut me out"
]


class Communion(KeywordAndModelConstruct):
    def __init__(self, tokenizer, model):
        super().__init__(
            "Communion",
            POSITIVE+NEGATIVE,
            POS_PHRASES+NEG_PHRASES,
            ["high communion","low communion"],
            tokenizer, model
        )
        self.pos=set(POSITIVE+POS_PHRASES)
        self.neg=set(NEGATIVE+NEG_PHRASES)

    def analyze_text(self, text):
        t = text.lower()
        p  = sum(1 for w in self.pos if w in t)
        n  = sum(1 for w in self.neg if w in t)
        raw = (p - n) / max(p + n, 1)
        kw  = 0.4 * ((raw + 1) / 2)
        zs  = 0.6 * self._zs_prob(
            t, ["strong relational themes", "detached narrative"]
        )
        return {self.name: {"CRS": (kw + zs) * 100,
                            "pos_hits": p, "neg_hits": n}}

