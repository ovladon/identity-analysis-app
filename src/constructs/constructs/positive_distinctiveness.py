# constructs/positive_distinctiveness.py
# ---------------------------------------------------------------------------
# Social Identity – Positive Distinctiveness (ingroup superiority)
# Tajfel & Turner 1979; Brown 2000.
# ---------------------------------------------------------------------------
from .keyword_and_model_construct import KeywordAndModelConstruct

KEYWORDS = [
    "superior", "superiority", "the best", "number one", "top tier",
    "top-tier", "unmatched", "ahead of", "better than", "excel", "excelled",
    "dominant", "dominance", "triumph", "first place", "outperform",
    "outperformed", "outperforms", "prevail", "prevails", "winning", "winner",
    "victorious", "victory", "elite", "prestige", "prestigious", "exceptional",
    "outstanding", "distinguished", "unique", "special", "sets us apart",
    "stand out", "proud of our group", "our excellence", "highest quality",
    "unsurpassed", "unrivalled", "finest", "finest team", "world-class",
    "world class", "state-of-the-art", "state of the art", "gold standard"
]

PHRASES = [
    "we are the best", "better than the rest", "beat them all",
    "ahead of the competition", "our superior group", "no one compares",
    "sets us apart from them", "top of the league", "cream of the crop"
]


class PositiveDistinctiveness(KeywordAndModelConstruct):
    def __init__(self, tokenizer, model):
        super().__init__(
            "PositiveDistinctiveness",
            KEYWORDS, PHRASES,
            ["ingroup superior", "ingroup not superior"],
            tokenizer, model
        )
        self.words=set(KEYWORDS+PHRASES)

    def analyze_text(self, text):
        t  = text.lower()
        kw = sum(1 for w in self.words if w in t) / len(self.words)
        zs = self._zs_prob(t, ["in-group is superior", "no superiority claim"])
        return {self.name: {"CRS": (0.4 * kw + 0.6 * zs) * 100}}

