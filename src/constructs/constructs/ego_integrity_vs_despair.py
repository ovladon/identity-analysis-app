# constructs/ego_integrity_vs_despair.py
# ---------------------------------------------------------------------------
# Erikson stage 8 (65+ yr) – Ego Integrity   ↔   Despair
# Sources: Ryff & Singer 1998; Whitbourne 1986; Erikson 1982.
# ---------------------------------------------------------------------------
from .keyword_and_model_construct import KeywordAndModelConstruct

POSITIVE = [
    "integrity", "ego integrity", "life review", "life reflection",
    "look back", "looking back", "content", "contentment", "satisfied",
    "fulfilment", "fulfilled", "peace", "at peace", "acceptance",
    "came to terms", "made peace", "wise", "wisdom", "gratitude",
    "gratified", "coherence", "coherent life", "meaningful life",
    "whole life", "purpose fulfilled", "no regrets", "thankful",
    "blessed", "rich life", "proud of my life", "completion", "wholeness"
]

NEGATIVE = [
    "despair", "regret", "regrets", "bitter", "bitterness",
    "disappointed", "disappointment", "disillusioned", "empty",
    "meaningless", "pointless", "wasted", "wasted life", "failure",
    "life of failure", "should have", "if only", "missed opportunities",
    "ashamed of life", "unfulfilled", "nothing to show", "no purpose",
    "couldn’t forgive", "unresolved", "resentment", "sorrow", "grief",
    "gloom", "hopeless", "gave up", "anguish", "torment", "lament"
]

POS_PHRASES = [
    "I’ve had a good life", "satisfied with my life", "made peace with",
    "life well lived", "nothing left undone", "sense of completion"
]

NEG_PHRASES = [
    "full of regret", "look back in anger", "wish I had",
    "I wasted my life", "too late now", "couldn’t forgive myself"
]


class EgoIntegrityVsDespair(KeywordAndModelConstruct):
    def __init__(self, tokenizer, model):
        super().__init__(
            "EgoIntegrityVsDespair",
            POSITIVE + NEGATIVE,
            POS_PHRASES + NEG_PHRASES,
            ["Integrity", "Despair"],
            tokenizer, model
        )
        self.pos=set(POSITIVE+POS_PHRASES)
        self.neg=set(NEGATIVE+NEG_PHRASES)

    def analyze_text(self, text):
        t=text.lower()
        pos=sum(1 for w in self.pos if w in t)
        neg=sum(1 for w in self.neg if w in t)
        raw=(pos-neg)/max(pos+neg,1)
        return {self.name:{"CRS":(raw+1)/2*100,
                           "pos_hits":pos,"neg_hits":neg}}

