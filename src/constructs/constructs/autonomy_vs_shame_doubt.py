# constructs/autonomy_vs_shame_doubt.py
# ---------------------------------------------------------------------------
# Erikson stage 2  (2-4 yr)  –  Autonomy   ↔   Shame / Doubt
# Sources: Erikson 1950; Kochanska et al. 1998 (self-control); Lewis 2002 (shame).
# ---------------------------------------------------------------------------
from .keyword_and_model_construct import KeywordAndModelConstruct

POSITIVE = [
    "autonomy", "independent", "self-reliant", "self reliant", "self-reliant",
    "on my own", "by myself", "own choice", "own decisions",
    "decided myself", "self-determined", "control", "controlled",
    "initiative", "assertive", "assert", "asserted", "mastered",
    "potty trained", "toilet trained", "tie my shoes", "dress myself",
    "feed myself", "freedom", "free", "explored", "exploring",
    "choose", "chose", "choosing", "selection", "selected",
    "confidence", "confident", "sure of myself", "capable", "competent",
    "self control", "self-control", "self regulation", "willpower"
]

NEGATIVE = [
    "shame", "ashamed", "embarrassed", "humiliated", "humiliation",
    "doubt", "self-doubt", "unsure", "uncertain", "timid", "fearful",
    "clingy", "overdependent", "dependent", "insecure", "fumble",
    "unable", "fail", "failed", "failure", "messy", "wet myself",
    "had an accident", "scolded", "scolding", "punished", "spilled",
    "broke it", "guilt", "guilty", "apologise", "sorry", "made fun of",
    "laughed at", "mocked", "teased", "ridiculed", "awkward",
    "no control", "helpless", "powerless"
]

POS_PHRASES = [
    "I can do it", "I did it myself", "let me try", "my decision",
    "took charge", "in control", "my own rules"
]

NEG_PHRASES = [
    "felt so ashamed", "full of doubt", "lost confidence", "made a mess",
    "wet the bed", "spilled everywhere", "was punished", "they laughed at me"
]


class AutonomyVsShameDoubt(KeywordAndModelConstruct):
    def __init__(self, tokenizer, model):
        super().__init__(
            "AutonomyVsShameDoubt",
            POSITIVE + NEGATIVE,
            POS_PHRASES + NEG_PHRASES,
            ["Autonomy", "Shame/Doubt"],
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

