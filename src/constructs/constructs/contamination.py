# constructs/contamination.py
# ---------------------------------------------------------------------------
# Narrative Identity – Contamination sequences (good → bad)
# Sources: McAdams et al. 2001.
# ---------------------------------------------------------------------------
from .keyword_and_model_construct import KeywordAndModelConstruct

KEYWORDS = [
    "contamination", "contaminate", "contaminated", "spoiled", "spoils",
    "tainted", "taint", "ruined", "ruin", "went downhill", "downhill",
    "fell apart", "fall apart", "shattered", "disaster", "nightmare",
    "bad turn", "dark turn", "turn for the worse", "good turned bad",
    "happy then sad", "bliss to misery", "dream became nightmare",
    "loss of innocence", "betrayed", "betrayal", "heartbreak", "collapse",
    "downfall", "deteriorated", "broken", "destroyed", "regret followed",
    "negative outcome", "went sour", "soured", "no happy ending"
]

PHRASES = [
    "everything fell apart", "started well but ended badly",
    "it all went downhill", "good times turned bad",
    "what seemed great became a nightmare"
]


class Contamination(KeywordAndModelConstruct):
    def __init__(self, tokenizer, model):
        super().__init__(
            "Contamination",
            KEYWORDS, PHRASES,
            ["contamination sequence","no contamination"],
            tokenizer, model
        )
        self.words=set(KEYWORDS+PHRASES)

    def analyze_text(self, text):
        t  = text.lower()
        kw = sum(1 for w in self.words if w in t) / len(self.words)
        zs = self._zs_prob(t, ["story turns bad", "no negative turn"])
        return {self.name: {"CRS": (0.4 * kw + 0.6 * zs) * 100}}

