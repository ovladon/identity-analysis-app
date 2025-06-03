# constructs/out_group_differentiation.py
# ---------------------------------------------------------------------------
# Social Identity – Out-Group Differentiation / Distance
# ---------------------------------------------------------------------------
from .keyword_and_model_construct import KeywordAndModelConstruct

KEYWORDS = [
    "they", "them", "their group", "those people", "outsider", "out-group",
    "outgroup", "foreigners", "foreign", "strangers", "not like us",
    "different from us", "alien", "others", "other side", "opposing group",
    "rival", "rivals", "enemy", "enemies", "competition", "competing group",
    "separate", "separated", "separates", "distinguish", "distinct",
    "distinctive", "distance ourselves", "draw a line", "keep out",
    "avoid them", "exclude", "excluded", "exclusion", "reject", "rejected",
    "they don’t belong", "they are not us", "divide", "division", "vs them"
]

PHRASES = [
    "us versus them", "keep them out", "those outsiders", "not one of us",
    "they’re different", "they’re not like us"
]


class OutGroupDifferentiation(KeywordAndModelConstruct):
    def __init__(self, tokenizer, model):
        super().__init__(
            "OutGroupDifferentiation",
            KEYWORDS, PHRASES,
            ["strong out-group differentiation","little out-group focus"],
            tokenizer, model
        )
        self.words=set(KEYWORDS+PHRASES)

    def analyze_text(self, text):
        t  = text.lower()
        kw = sum(1 for w in self.words if w in t) / len(self.words)
        zs = self._zs_prob(t, ["emphasises differences with outgroup", "no outgroup emphasis"])
        return {self.name: {"CRS": (0.4 * kw + 0.6 * zs) * 100}}


