# constructs/identity_achievement.py
# ---------------------------------------------------------------------------
# Marcia status – Identity Achievement
# Sources: Marcia 1966; Kroger & Marcia 2011; Meeus 2011.
# ---------------------------------------------------------------------------
from .keyword_and_model_construct import KeywordAndModelConstruct

KEYWORDS = [
    "identity achieved", "achieved identity", "settled on", "decided on",
    "made up my mind", "after exploring", "after much thought", "self-chosen",
    "own choice", "committed", "commitment", "commitments", "established",
    "formed identity", "clarified", "clear sense of self", "resolved",
    "integrated", "integrated identity", "stable identity", "coherent identity",
    "found my path", "know who I am", "know what I want", "firm beliefs",
    "personal values", "chose for myself", "authentic", "self-definition",
    "confident identity", "confirmed identity"
]

PHRASES = [
    "I explored my options before deciding", "I chose my career after careful thought",
    "I committed to", "having considered many alternatives", "finally resolved",
    "came to a conclusion about who I am"
]


class IdentityAchievement(KeywordAndModelConstruct):
    def __init__(self, tokenizer, model):
        super().__init__(
            "IdentityAchievement",
            KEYWORDS,
            PHRASES,
            ["achievement", "other"],
            tokenizer, model
        )
        self.words=set(KEYWORDS+PHRASES)

    def analyze_text(self, text):
        t  = text.lower()
        kw = sum(1 for w in self.words if w in t) / len(self.words)
        zs = self._zs_prob(t, ["identity achievement", "identity not achieved"])
        return {self.name: {"CRS": (0.4 * kw + 0.6 * zs) * 100}}

