"""
constructs/__init__.py
Initialises every construct detector (23 total) and exposes
`construct_objects` for the rest of the application.
"""

# ────────────────────────────────────────────────────────────────────────────
#  1.  Import detector classes
# ────────────────────────────────────────────────────────────────────────────
# Erikson stages
from .trust_vs_mistrust          import TrustVsMistrust
from .autonomy_vs_shame_doubt    import AutonomyVsShameDoubt
from .initiative_vs_guilt        import InitiativeVsGuilt
from .industry_vs_inferiority    import IndustryVsInferiority
from .identity_vs_role_confusion import IdentityVsRoleConfusion
from .intimacy_vs_isolation      import IntimacyVsIsolation
from .generativity_vs_stagnation import GenerativityVsStagnation
from .ego_integrity_vs_despair   import EgoIntegrityVsDespair

# Marcia statuses
from .identity_achievement  import IdentityAchievement
from .identity_moratorium   import IdentityMoratorium
from .identity_foreclosure  import IdentityForeclosure
from .identity_diffusion    import IdentityDiffusion

# Social-Identity
from .in_group_identification   import InGroupIdentification
from .out_group_differentiation import OutGroupDifferentiation
from .positive_distinctiveness  import PositiveDistinctiveness

# Narrative-Identity
from .agency        import Agency
from .communion     import Communion
from .redemption    import Redemption
from .contamination import Contamination
from .meaning_making import MeaningMaking

# Self-Concept
from .actual_self import ActualSelf
from .ideal_self  import IdealSelf
from .ought_self  import OughtSelf


# ────────────────────────────────────────────────────────────────────────────
#  2.  Shared model + tokenizer + zero-shot pipeline
# ────────────────────────────────────────────────────────────────────────────
from model_loader import model_loader          # singleton created there

tokenizer = model_loader.get_tokenizer()
model     = model_loader.get_model()           # SimCSE encoder
# BART MNLI zero-shot is available as model_loader.zero_shot_pipe
# (detectors access it via self.zero_shot in their base class)


# ────────────────────────────────────────────────────────────────────────────
#  3.  Instantiate one detector per construct
# ────────────────────────────────────────────────────────────────────────────
construct_objects = {
    # Erikson (8)
    "TrustVsMistrust"         : TrustVsMistrust(tokenizer, model),
    "AutonomyVsShameDoubt"    : AutonomyVsShameDoubt(tokenizer, model),
    "InitiativeVsGuilt"       : InitiativeVsGuilt(tokenizer, model),
    "IndustryVsInferiority"   : IndustryVsInferiority(tokenizer, model),
    "IdentityVsRoleConfusion" : IdentityVsRoleConfusion(tokenizer, model),
    "IntimacyVsIsolation"     : IntimacyVsIsolation(tokenizer, model),
    "GenerativityVsStagnation": GenerativityVsStagnation(tokenizer, model),
    "EgoIntegrityVsDespair"   : EgoIntegrityVsDespair(tokenizer, model),

    # Marcia (4)
    "IdentityAchievement" : IdentityAchievement(tokenizer, model),
    "IdentityMoratorium"  : IdentityMoratorium(tokenizer, model),
    "IdentityForeclosure" : IdentityForeclosure(tokenizer, model),
    "IdentityDiffusion"   : IdentityDiffusion(tokenizer, model),

    # Social-Identity (3)
    "InGroupIdentification"   : InGroupIdentification(tokenizer, model),
    "OutGroupDifferentiation" : OutGroupDifferentiation(tokenizer, model),
    "PositiveDistinctiveness" : PositiveDistinctiveness(tokenizer, model),

    # Narrative-Identity (5)
    "Agency"        : Agency(tokenizer, model),
    "Communion"     : Communion(tokenizer, model),
    "Redemption"    : Redemption(tokenizer, model),
    "Contamination" : Contamination(tokenizer, model),
    "MeaningMaking" : MeaningMaking(tokenizer, model),

    # Self-Concept (3)
    "ActualSelf" : ActualSelf(tokenizer, model),
    "IdealSelf"  : IdealSelf(tokenizer, model),
    "OughtSelf"  : OughtSelf(tokenizer, model),
}

