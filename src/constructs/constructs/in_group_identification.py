# constructs/in_group_identification.py
# ---------------------------------------------------------------------------
# Social Identity – In-Group Identification  (revised: added tribal solidarity words)
# ---------------------------------------------------------------------------
from .keyword_and_model_construct import KeywordAndModelConstruct

KEYWORDS = [
    "we", "us", "our", "ours", "ingroup", "in-group", "my group", "our group",
    "tribe", "clan", "band", "my band", "our band", "my tribe", "my people",
    "our people", "fellow", "comrades", "teammate", "belong", "belonging",
    "member of", "membership", "part of", "one of us", "identify with",
    "identification", "solidarity", "unity", "together", "togetherness",
    "collective", "loyal", "loyalty", "faithful", "bond with", "attached to",
    "group pride", "group honour", "group honor", "commitment to group",
    "defend our", "support our", "stand with", "stood with", "us all"
]

PHRASES = [
    "we stand together", "proud member of", "sense of belonging",
    "identify strongly with", "part of our community", "our shared identity"
]


class InGroupIdentification(KeywordAndModelConstruct):
    def __init__(self, tokenizer, model):
        super().__init__(
            "InGroupIdentification",
            KEYWORDS, PHRASES,
            ["strong in-group identity", "weak in-group identity"],
            tokenizer, model
        )
        self.words = set(KEYWORDS + PHRASES)

    def analyze_text(self, text):
        t = text.lower()
        kw = sum(1 for w in self.words if w in t) / len(self.words)
        zs = self._zs_prob(
            t, ["I identify with my group", "group identity not salient"]
        )
        return {self.name: {"CRS": (0.4 * kw + 0.6 * zs) * 100}}

