# constructs/trust_vs_mistrust.py
# ---------------------------------------------------------------------------
# Erikson stage 1  (0-2 yr)  –  Trust   ↔   Mistrust
# Lexicon sources: Erikson 1950; Main & Goldwyn 1984; Hazan & Shaver 1987.
# ---------------------------------------------------------------------------
from .keyword_and_model_construct import KeywordAndModelConstruct

POSITIVE = [
    # security / warmth
    "trust", "trusted", "trusting", "secure", "security", "safe", "safety",
    "protected", "protective", "cared", "caregiver", "looked after",
    "nurtured", "reliable", "dependable", "faith", "confident", "comfort",
    "comforted", "bonded", "attachment", "attached", "supported", "supportive",
    "held", "embraced", "soothed", "soothing", "welcome", "welcomed",
    "fed on time", "responded to", "consistent", "predictable", "loving",
    "affectionate", "responsive", "attentive", "available", "present",
    "there for me", "had my back", "stood by me", "count on", "counted on",
    "reassured", "depend on", "dependable", "faithful", "secure base"
]

NEGATIVE = [
    # mistrust / neglect
    "mistrust", "mistrusted", "suspicious", "wary", "wariness",
    "unsafe", "unprotected", "exposed", "abandoned", "neglected",
    "ignored", "unattended", "unreliable", "inconsistent", "unpredictable",
    "betrayed", "betray", "let down", "lied to", "deceived", "dishonest",
    "fearful", "scared", "terror", "distrust", "distrusted",
    "cold", "distant", "aloof", "absent", "withheld affection",
    "unavailable", "left alone", "cry alone", "isolated", "neglectful",
    "abuse", "abused", "hurt", "harm", "threat", "threatened",
    "no one there", "nobody there", "couldn’t rely", "no faith"
]

POS_PHRASES = [
    "felt safe", "felt secure", "could rely on", "was always there",
    "took care of me", "rocked me", "soothed me", "met my needs",
    "warm embrace", "steady presence"
]

NEG_PHRASES = [
    "left to cry", "no one came", "couldn’t trust", "broken promise",
    "let me down", "felt abandoned", "felt unsafe", "withheld love",
    "never knew if", "fear of being hurt"
]


class TrustVsMistrust(KeywordAndModelConstruct):
    def __init__(self, tokenizer, model):
        super().__init__(
            "TrustVsMistrust",
            POSITIVE + NEGATIVE,
            POS_PHRASES + NEG_PHRASES,
            ["Trust", "Mistrust"],
            tokenizer, model
        )
        self.pos_words = set(POSITIVE + POS_PHRASES)
        self.neg_words = set(NEGATIVE + NEG_PHRASES)

    # ---------------------------------------------------------------------
    def analyze_text(self, text: str):
        lower_text = text.lower()
        pos_hits = sum(1 for w in self.pos_words if w in lower_text)
        neg_hits = sum(1 for w in self.neg_words if w in lower_text)
        raw = (pos_hits - neg_hits) / max(pos_hits + neg_hits, 1)
        crs = (raw + 1) / 2 * 100    # map -1…+1 → 0…100
        return {self.name: {"CRS": crs,
                            "pos_hits": pos_hits,
                            "neg_hits": neg_hits}}

