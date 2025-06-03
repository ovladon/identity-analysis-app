# constructs/identity_vs_role_confusion.py
# ---------------------------------------------------------------------------
# Erikson stage 5 (12-18 yr) – Identity Cohesion   ↔   Role Confusion
# Sources: Erikson 1968; Marcia 1966 status interviews; Schwartz et al. 2011.
# ---------------------------------------------------------------------------
from .keyword_and_model_construct import KeywordAndModelConstruct

POSITIVE = [
    "identity", "identity achieved", "self-definition", "defined myself",
    "sense of self", "who I am", "figured myself out", "coherent self",
    "consistent self", "authentic", "values", "commitment", "direction",
    "purpose", "knowing my path", "clear future", "career choice",
    "life goal", "belong", "belonging", "fidelity", "integrated", "solid",
    "stable", "certainty", "confident in who I am"
]

NEGATIVE = [
    "role confusion", "identity confusion", "confused", "lost", "lost self",
    "don’t know who I am", "mixed up", "no idea", "searching for identity",
    "trying to find myself", "in crisis", "identity crisis", "undefined",
    "fragmented", "empty", "aimless", "drifting", "wandering",
    "no direction", "uncertain", "contradictory", "false self", "fake",
    "pretend", "imitate", "copying others", "negative identity", "rebellion"
]

POS_PHRASES = [
    "I know who I am", "I found myself", "I forged my own path",
    "I am true to myself", "my chosen identity", "self-coherent narrative"
]

NEG_PHRASES = [
    "who am I", "I feel lost", "searching for meaning", "living a lie",
    "don’t fit in", "feel empty", "adopting roles", "masking myself"
]


class IdentityVsRoleConfusion(KeywordAndModelConstruct):
    def __init__(self, tokenizer, model):
        super().__init__(
            "IdentityVsRoleConfusion",
            POSITIVE + NEGATIVE,
            POS_PHRASES + NEG_PHRASES,
            ["Identity", "Role Confusion"],
            tokenizer, model
        )
        self.pos=set(POSITIVE+POS_PHRASES)
        self.neg=set(NEGATIVE+NEG_PHRASES)

    def analyze_text(self,text):
        t=text.lower()
        pos=sum(1 for w in self.pos if w in t)
        neg=sum(1 for w in self.neg if w in t)
        raw=(pos-neg)/max(pos+neg,1)
        return {self.name:{"CRS":(raw+1)/2*100,
                           "pos_hits":pos,"neg_hits":neg}}

