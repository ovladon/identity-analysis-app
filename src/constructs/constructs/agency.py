# constructs/agency.py
# ---------------------------------------------------------------------------
# Narrative Identity – Agency (mastery, control)
# Added military-leadership verbs: led, commanded, raided, defended, etc.
# ---------------------------------------------------------------------------
from .keyword_and_model_construct import KeywordAndModelConstruct

POSITIVE = [
    "agency", "agentic", "took charge", "took control", "in control",
    "controlled", "commanded", "command", "commander", "directed",
    "led", "lead", "led the", "lead the", "leadership", "headed", "captained",
    "initiated", "instigated", "spearheaded", "drove", "drive", "driven",
    "took the wheel", "mastered", "mastery", "founded", "established", "built",
    "created", "constructed", "launched", "kickstarted", "orchestrated",
    "organized", "organised", "planned", "strategised", "strategized",
    "decided", "determined", "resolved", "made it happen", "achieved",
    "accomplished", "earned", "succeeded", "triumphed", "victorious",
    "assertive", "asserted", "took initiative", "self-starter",
    "entrepreneurial", "proactive", "pursued", "chased", "forged",
    "carved out", "paved the way", "overcame", "overcome", "persevered",
    "strived", "pushed through", "ambitious", "ambition", "goal-oriented",
    "took responsibility", "my decision", "my choice",
    # new warfare / leadership verbs
    "raided", "raid", "organized a raid", "led a raid", "defended",
    "defend", "defending", "mounted", "mounted an attack", "countered",
    "marshalled", "mobilised", "mobilized"
]

NEGATIVE = [
    "passive", "passivity", "drifted", "drifting", "reactive",
    "victim", "victimhood", "helpless", "helplessness", "powerless",
    "no control", "out of control", "couldn’t help", "forced to",
    "made me", "had to", "was told", "went along", "followed orders",
    "no choice", "stuck with", "directionless", "aimless", "apathetic"
]

PHRASES_POS = [
    "I made it happen", "I took matters into my own hands",
    "I seized the opportunity", "I stepped up", "I forged ahead",
    "I charted my own course"
]

PHRASES_NEG = [
    "nothing I could do", "out of my hands", "beyond my control",
    "I just went with it", "I had no say", "I was pushed around"
]


class Agency(KeywordAndModelConstruct):
    def __init__(self, tokenizer, model):
        super().__init__(
            "Agency",
            POSITIVE + NEGATIVE,
            PHRASES_POS + PHRASES_NEG,
            ["agentic", "passive"],
            tokenizer, model
        )
        self.pos = set(POSITIVE + PHRASES_POS)
        self.neg = set(NEGATIVE + PHRASES_NEG)

    def analyze_text(self, text):
        t   = text.lower()
        pos = sum(1 for w in self.pos if w in t)
        neg = sum(1 for w in self.neg if w in t)
        raw = (pos - neg) / max(pos + neg, 1)
        kw_part = 0.4 * ((raw + 1) / 2)
        zs_part = 0.6 * self._zs_prob(
            t, ["high personal agency", "little personal agency"]
        )
        return {self.name: {"CRS": (kw_part + zs_part) * 100,
                            "pos_hits": pos, "neg_hits": neg}}

