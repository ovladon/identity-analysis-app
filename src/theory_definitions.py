"""
Enriched theory definitions file.
Each construct entry has:
  description          – neutral definition
  high_interpretation  – what a high CRS (>50) means
  low_interpretation   – what a low CRS (<30) means
  markers              – prototypical lexical cues (for tooltip display)
  age_range            – developmental age range where construct is normative / salient
  reference            – APA citation
  doi                  – DOI or URL if available
"""

theory_definitions = {
    "Erikson's Psychosocial Development": {
        "description": "Eight sequential psychosocial crises from infancy to late adulthood (Erikson, 1950, 1963, 1968).",
        "constructs": {
            "TrustVsMistrust": {
                "description": "Confidence that caregivers will reliably meet basic needs.",
                "high_interpretation": "Secure stance toward others; willingness to rely on relationships.",
                "low_interpretation": "Basic wariness and difficulty relying on others.",
                "markers": ["trust", "secure base", "felt safe", "reliable support"],
                "age_range": "0–2 yrs",
                "reference": ["Erikson, E. H. (1950). Childhood and Society."],
                "doi": "10.1037/13033-000"
            },
            "AutonomyVsShameDoubt": {
                "description": "Formation of will and self‑control versus feelings of shame or doubt in ability.",
                "high_interpretation": "Acts independently, takes initiative in age‑appropriate tasks.",
                "low_interpretation": "Easily shamed or doubtful about abilities.",
                "markers": ["do it myself", "control", "own choice", "ashamed"],
                "age_range": "2–4 yrs",
                "reference": ["Erikson, 1950/1963."],
                "doi": "N/A"
            },
            "InitiativeVsGuilt": {
                "description": "Assertive pursuit of goals balanced against guilt over mis‑steps.",
                "high_interpretation": "Energetic planning and enterprise.",
                "low_interpretation": "Hesitant initiative, frequent guilt.",
                "markers": ["plan games", "decide", "guilty", "took charge"],
                "age_range": "4–6 yrs",
                "reference": ["Erikson, 1950."],
                "doi": "N/A"
            },
            "IndustryVsInferiority": {
                "description": "Sense of competence in valued skills vs. feelings of inadequacy.",
                "high_interpretation": "Pride in completed work and skills.",
                "low_interpretation": "Sense of being less capable than peers.",
                "markers": ["accomplishment", "proud of my work", "failed at school"],
                "age_range": "6–12 yrs",
                "reference": ["Erikson, 1950."],
                "doi": "N/A"
            },
            "IdentityVsRoleConfusion": {
                "description": "Integration of self‑concept or diffusion and confusion about future roles.",
                "high_interpretation": "Coherent sense of self, commitments, fidelity.",
                "low_interpretation": "Uncertainty or incoherence about personal identity.",
                "markers": ["identity crisis", "who am I?", "found myself"],
                "age_range": "12–18 yrs",
                "reference": ["Erikson, 1968. Identity: Youth and Crisis."],
                "doi": "N/A"
            },
            "IntimacyVsIsolation": {
                "description": "Capacity for close mutual relationships versus social isolation.",
                "high_interpretation": "Sustains deep, reciprocal intimacy.",
                "low_interpretation": "Avoids closeness; feels lonely.",
                "markers": ["close relationship", "open up", "lonely", "isolate"],
                "age_range": "18–40 yrs",
                "reference": ["Erikson, 1968."],
                "doi": "N/A"
            },
            "GenerativityVsStagnation": {
                "description": "Productive concern for next generation versus self‑absorption and stagnation.",
                "high_interpretation": "Mentoring, creating, caring for others.",
                "low_interpretation": "Self‑focused, sense of being stuck.",
                "markers": ["mentor", "legacy", "stuck", "self‑absorbed"],
                "age_range": "40–65 yrs",
                "reference": ["Erikson, 1950."],
                "doi": "N/A"
            },
            "EgoIntegrityVsDespair": {
                "description": "Acceptance of one’s life cycle versus regret and despair.",
                "high_interpretation": "Peaceful life review, wisdom.",
                "low_interpretation": "Widespread regret, bitterness.",
                "markers": ["look back", "content", "regret", "despair"],
                "age_range": "65 yrs +",
                "reference": ["Erikson, 1968."],
                "doi": "N/A"
            }
        }
    },
    "Marcia's Identity Status Theory": {
        "description": "Operationalisation of Erikson's adolescent stage using exploration × commitment matrix.",
        "constructs": {
            "IdentityDiffusion": {
                "description": "Low exploration, low commitment.",
                "high_interpretation": "n/a – lack of commitment is the defining property.",
                "low_interpretation": "Opposite of diffusion (i.e., some structure).",
                "markers": ["don't know", "no idea", "whatever", "drifting"],
                "age_range": "12–18 yrs",
                "reference": ["Marcia, J. E. (1966). Development and validation of ego‑identity status."],
                "doi": "10.1037/h0023281"
            },
            "IdentityForeclosure": {
                "description": "Commitment without prior exploration.",
                "high_interpretation": "Strong, often borrowed commitments.",
                "low_interpretation": "Openness to explore, flexibility.",
                "markers": ["never questioned", "family expects", "pre-set path"],
                "age_range": "12–18 yrs",
                "reference": ["Marcia, 1966."],
                "doi": "10.1037/h0023281"
            },
            "IdentityMoratorium": {
                "description": "High exploration, low commitment (the active crisis).",
                "high_interpretation": "Engaged search for identity.",
                "low_interpretation": "Premature closure or apathy.",
                "markers": ["trying out", "still deciding", "in flux"],
                "age_range": "12–18 yrs",
                "reference": ["Marcia, 1966."],
                "doi": "10.1037/h0023281"
            },
            "IdentityAchievement": {
                "description": "Commitment following exploration.",
                "high_interpretation": "Self‑chosen values and goals.",
                "low_interpretation": "No firm commitments.",
                "markers": ["decided", "found my path", "chose"],
                "age_range": "16 yrs +",
                "reference": ["Marcia, 1966."],
                "doi": "10.1037/h0023281"
            }
        }
    },
    "Social Identity Theory": {
        "description": "Identity derived from group membership, social categorisation and comparison.",
        "constructs": {
            "InGroupIdentification": {
                "description": "Psychological attachment to an in‑group.",
                "high_interpretation": "Strong feeling of belonging and loyalty.",
                "low_interpretation": "Weak or no in‑group salience.",
                "markers": ["we", "our people", "part of", "member of"],
                "age_range": "all ages",
                "reference": ["Tajfel & Turner (1979)."],
                "doi": "N/A"
            },
            "OutGroupDifferentiation": {
                "description": "Perceptual, affective or behavioural separation from out‑groups.",
                "high_interpretation": "Frequent emphasis on difference or distance.",
                "low_interpretation": "Little out‑group focus.",
                "markers": ["they", "those people", "different from us"],
                "age_range": "all ages",
                "reference": ["Tajfel & Turner (1979)."],
                "doi": "N/A"
            },
            "PositiveDistinctiveness": {
                "description": "Motivated effort to view the in‑group as superior.",
                "high_interpretation": "Consistent claims of in‑group superiority.",
                "low_interpretation": "Neutral or negative in‑group evaluation.",
                "markers": ["better than", "number one", "superior", "ahead of them"],
                "age_range": "all ages",
                "reference": ["Tajfel & Turner (1979)."],
                "doi": "N/A"
            }
        }
    },
    "Narrative Identity Theory": {
        "description": "Identity constructed as an internalised, evolving life story (McAdams).",
        "constructs": {
            "Agency": {
                "description": "Themes of mastery, achievement, responsible self‑assertion.",
                "high_interpretation": "Narrative dominated by personal control and success.",
                "low_interpretation": "Little sense of personal efficacy.",
                "markers": ["took charge", "made it happen", "overcame"],
                "age_range": "adolescence +",
                "reference": ["McAdams, D. P. (2001). The psychology of life stories."],
                "doi": "10.1037/1089-2680.5.2.100"
            },
            "Communion": {
                "description": "Themes of love, friendship, dialogue and connection.",
                "high_interpretation": "Strong relational and affiliative focus.",
                "low_interpretation": "Narrative of detachment or conflict.",
                "markers": ["together", "bond", "support", "we cared"],
                "age_range": "adolescence +",
                "reference": ["McAdams, 2001."],
                "doi": "10.1037/1089-2680.5.2.100"
            },
            "Redemption": {
                "description": "Bad scenes turn good; suffering leads to growth.",
                "high_interpretation": "Frequent redemption arcs.",
                "low_interpretation": "Few or no redemptive sequences.",
                "markers": ["blessing in disguise", "turned out well", "made me stronger"],
                "age_range": "all ages",
                "reference": ["McAdams et al. (2001)."],
                "doi": "10.1111/1467-6494.00443"
            },
            "Contamination": {
                "description": "Good scenes turn bad; positive turned sour.",
                "high_interpretation": "Frequent contamination arcs.",
                "low_interpretation": "Few or no contamination sequences.",
                "markers": ["went downhill", "ruined everything", "spoiled the moment"],
                "age_range": "all ages",
                "reference": ["McAdams et al. (2001)."],
                "doi": "10.1111/1467-6494.00443"
            },
            "MeaningMaking": {
                "description": "Explicit lessons or insights drawn from events.",
                "high_interpretation": "Highly reflective, lesson‑oriented narrative.",
                "low_interpretation": "Events told with minimal reflection.",
                "markers": ["I learned that", "made me realise", "taught me"],
                "age_range": "adolescence +", 
                "reference": ["Habermas & Bluck (2000)."],
                "doi": "10.1037/0033-2909.126.5.748"
            }
        }
    },
    "Self-Concept Theory": {
        "description": "Individual’s organised beliefs and evaluations about the self.",
        "constructs": {
            "ActualSelf": {
                "description": "Perceived attributes that one believes one actually possesses.",
                "high_interpretation": "Clear, confident description of current self.",
                "low_interpretation": "Vague or conflicted self‑description.",
                "markers": ["I am", "my self‑image", "the real me"],
                "age_range": "all ages",
                "reference": ["Rosenberg, M. (1979). Conceiving the self."],
                "doi": "N/A"
            },
            "IdealSelf": {
                "description": "Attributes one would ideally like to possess.",
                "high_interpretation": "Strong, clear aspirations.",
                "low_interpretation": "Few or undefined aspirations.",
                "markers": ["I wish", "I want to be", "my dream self"],
                "age_range": "all ages",
                "reference": ["Higgins, E. T. (1987). Self‑discrepancy theory."],
                "doi": "10.1037/0033-295X.94.3.319"
            },
            "OughtSelf": {
                "description": "Attributes one believes they should possess (duties, obligations).",
                "high_interpretation": "Narrative saturated with duty, ‘must’, obligations.",
                "low_interpretation": "Few explicit ought‑self statements.",
                "markers": ["I should", "I must", "expected of me"],
                "age_range": "all ages",
                "reference": ["Higgins, 1987."],
                "doi": "10.1037/0033-295X.94.3.319"
            }
        }
    }
}

def find_construct_description(name: str):
    for model in theory_definitions.values():
        if 'constructs' in model and name in model['constructs']:
            return model['constructs'][name]
    return {}
