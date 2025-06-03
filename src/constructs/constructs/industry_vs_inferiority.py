# constructs/industry_vs_inferiority.py
# ---------------------------------------------------------------------------
# Erikson stage 4  (6-12 yr) – Industry   ↔   Inferiority
# Sources: Erikson 1950; Eccles 1993 (competence); Elliot & Dweck 2005.
# ---------------------------------------------------------------------------
from .keyword_and_model_construct import KeywordAndModelConstruct

POSITIVE = [
    "industry", "industrious", "hardworking", "hard-working", "diligent",
    "diligence", "competent", "competence", "skilled", "skillful", "mastery",
    "craftsmanship", "built", "constructed", "produced", "productive",
    "achievement", "accomplishment", "earned", "effort", "practice", "practiced",
    "improved", "progress", "finished", "completed", "successful",
    "badge", "award", "proud of my work", "good grades", "top of class",
    "talent", "ability", "gifted", "excel", "excelled", "exceling", "competitions",
    "learned", "studied", "studious", "trained", "training"
]

NEGATIVE = [
    "inferior", "inferiority", "incompetent", "inadequate", "inapt",
    "failure", "failed", "fail", "failing", "worthless", "useless",
    "stupid", "dumb", "slow", "behind", "last place", "poor grades",
    "couldn’t keep up", "lagged", "clumsy", "awkward", "messed up",
    "unfinished", "unskilled", "no talent", "weakness", "defeated",
    "defeat", "lost", "loser", "rejected work", "criticised work",
    "scolded for mistakes", "can’t do anything right"
]

POS_PHRASES = [
    "proud of my work", "sense of accomplishment", "job well done",
    "fixed it", "built from scratch", "completed the project", "earned praise"
]

NEG_PHRASES = [
    "not good enough", "fell behind", "looked stupid", "felt worthless",
    "failed miserably", "kept making mistakes", "couldn’t finish"
]


class IndustryVsInferiority(KeywordAndModelConstruct):
    def __init__(self, tokenizer, model):
        super().__init__(
            "IndustryVsInferiority",
            POSITIVE + NEGATIVE,
            POS_PHRASES + NEG_PHRASES,
            ["Industry", "Inferiority"],
            tokenizer, model
        )
        self.pos=set(POSITIVE+POS_PHRASES)
        self.neg=set(NEGATIVE+NEG_PHRASES)

    def analyze_text(self,text):
        t=text.lower()
        pos=sum(1 for w in self.pos if w in t)
        neg=sum(1 for w in self.neg if w in t)
        raw=(pos-neg)/max(pos+neg,1)
        return {self.name:{"CRS":(raw+1)/2*100,
                           "pos_hits":pos,"neg_hits":neg}}

