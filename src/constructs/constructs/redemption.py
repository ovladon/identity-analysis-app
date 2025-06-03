# constructs/redemption.py
# ---------------------------------------------------------------------------
# Narrative Identity – Redemption sequences (bad → good)
# Sources: McAdams et al. 2001; McAdams 2006 "Redemptive Self".
# ---------------------------------------------------------------------------
from .keyword_and_model_construct import KeywordAndModelConstruct

KEYWORDS = [
    "redeem", "redeemed", "redemption", "overcame", "overcome", "overcoming",
    "bounced back", "bounce back", "recovered", "recovery", "rebound",
    "turned around", "turnaround", "silver lining", "blessing in disguise",
    "made me stronger", "grew from", "growth through adversity",
    "triumphed over", "rose above", "rise above", "phoenix", "out of ashes",
    "transformed", "transformation", "turned my life around", "good came out",
    "lesson learned", "moral learned", "found purpose in pain",
    "turned hardship into", "benefit from failure", "bad turned good",
    "positive outcome", "uplift", "redemptive arc", "rags to riches",
    "from darkness to light", "reclaimed", "second chance", "catharsis"
]

PHRASES = [
    "what seemed awful became a blessing", "something good came out of",
    "at first a setback, ultimately a victory", "made the best of",
    "out of the worst situation", "ended up better off"
]


class Redemption(KeywordAndModelConstruct):
    def __init__(self, tokenizer, model):
        super().__init__(
            "Redemption",
            KEYWORDS, PHRASES,
            ["redemptive sequence","no redemption"],
            tokenizer, model
        )
        self.words=set(KEYWORDS+PHRASES)

    def analyze_text(self, text):
        t  = text.lower()
        kw = sum(1 for w in self.words if w in t) / len(self.words)
        zs = self._zs_prob(t, ["story of redemption", "no redemption arc"])
        return {self.name: {"CRS": (0.4 * kw + 0.6 * zs) * 100}}

