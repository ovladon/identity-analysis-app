# constructs/initiative_vs_guilt.py
# ---------------------------------------------------------------------------
# Erikson stage 3  (4-6 yr)  –  Initiative   ↔   Guilt
# Sources: Erikson 1950; McClelland 1961 (nAch verbs); Hayes & Casey 1996.
# ---------------------------------------------------------------------------
from .keyword_and_model_construct import KeywordAndModelConstruct

POSITIVE = [
    "initiative", "initiated", "took initiative", "lead", "led",
    "leadership", "started", "launched", "set up", "organized", "planned",
    "scheme", "creative play", "invented", "imagined", "exploit",
    "adventure", "make-believe", "storytelling", "took the lead",
    "ran the game", "decided", "determined", "volunteered", "proactive",
    "drive", "spark", "ambition", "goal", "purposeful", "drove",
    "pursued", "chased", "exploration", "quest", "bold", "daring"
]

NEGATIVE = [
    "guilt", "guilty", "ashamed", "regret", "sorry", "felt bad",
    "self blame", "blamed myself", "bothered me", "remorse",
    "shouldn’t have", "wrong", "wrongful", "naughty", "mischief",
    "punished", "told off", "scolded", "trespass", "transgression",
    "lied", "lying", "steal", "stole", "stealing", "hurt someone",
    "hit", "fought", "disobeyed", "disobedient", "broke a rule",
    "violation", "offense", "mistake", "errors", "regretted"
]

POS_PHRASES = [
    "started a game", "took charge of the game", "came up with",
    "made a plan", "let's pretend", "let us play", "I volunteer",
    "I will do it", "set out to", "took the first step"
]

NEG_PHRASES = [
    "felt so guilty", "I shouldn’t have", "I was in trouble",
    "got punished", "felt ashamed", "overwhelmed by guilt",
    "remorse for", "apologised for"
]


class InitiativeVsGuilt(KeywordAndModelConstruct):
    def __init__(self, tokenizer, model):
        super().__init__(
            "InitiativeVsGuilt",
            POSITIVE + NEGATIVE,
            POS_PHRASES + NEG_PHRASES,
            ["Initiative", "Guilt"],
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

