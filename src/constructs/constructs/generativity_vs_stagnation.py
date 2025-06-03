# constructs/generativity_vs_stagnation.py
# ---------------------------------------------------------------------------
# Erikson stage 7 (40–65 yr) – Generativity   ↔   Stagnation
# Sources: McAdams & de St. Aubin 1992; Gruenewald et al. 2004.
# ---------------------------------------------------------------------------
from .keyword_and_model_construct import KeywordAndModelConstruct

POSITIVE = [
    "generativity", "generative", "mentor", "mentoring", "mentored",
    "guide", "guiding", "coaching", "coach", "teach", "taught", "teaching",
    "nurture", "nurtured", "raising", "raise", "parenting", "children",
    "next generation", "legacy", "leave a legacy", "contribute",
    "contributing", "contribution", "philanthropy", "philanthropic",
    "charity", "charitable", "endow", "endowment", "endowed", "donate",
    "donated", "donation", "volunteer", "volunteered", "service",
    "community service", "give back", "giving back", "supporting others",
    "helping others", "building", "creating", "productivity", "productive",
    "bequeath", "establish", "established", "foster", "cultivate",
    "develop others", "succession", "stewardship", "make a difference"
]

NEGATIVE = [
    "stagnation", "stagnant", "stuck", "idle", "bored", "self-absorbed",
    "self absorbed", "selfish", "self-centered", "midlife crisis", "apathetic",
    "aimless", "going nowhere", "no purpose", "no direction", "narcissistic",
    "unproductive", "waste time", "lost decade", "nothing to show",
    "regret wasted", "felt useless", "felt empty", "burned out", "burnout",
    "routine", "monotony", "no growth", "no development", "plateaued",
    "lack of progress", "stalled", "dormant", "dead end"
]

POS_PHRASES = [
    "gave scholarships", "funded a library", "started a foundation",
    "mentored young people", "supported the community", "left a legacy",
    "invested in the next generation"
]

NEG_PHRASES = [
    "felt stuck in a rut", "going through the motions",
    "nothing meaningful", "my life stalled", "hit a dead end"
]


class GenerativityVsStagnation(KeywordAndModelConstruct):
    def __init__(self, tokenizer, model):
        super().__init__(
            "GenerativityVsStagnation",
            POSITIVE + NEGATIVE,
            POS_PHRASES + NEG_PHRASES,
            ["Generativity", "Stagnation"],
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

