# visualization.py
# ---------------------------------------------------------------------------
# Sunburst constructor + optional on-screen display + PNG saver
# Requires plotly>=5.12, kaleido>=0.2 for static export
# ---------------------------------------------------------------------------
import plotly.express as px
import pandas as pd
import plotly.io as pio
import streamlit as st

MODEL_MAPPING = {
    "Erikson's Psychosocial Development": [
        'TrustVsMistrust', 'AutonomyVsShameDoubt', 'InitiativeVsGuilt',
        'IndustryVsInferiority', 'IdentityVsRoleConfusion',
        'IntimacyVsIsolation', 'GenerativityVsStagnation',
        'EgoIntegrityVsDespair'
    ],
    "Marcia's Identity Status Theory": [
        'IdentityAchievement', 'IdentityMoratorium',
        'IdentityForeclosure', 'IdentityDiffusion'
    ],
    "Social Identity Theory": [
        'InGroupIdentification', 'OutGroupDifferentiation',
        'PositiveDistinctiveness'
    ],
    "Narrative Identity Theory": [
        'Agency', 'Communion', 'Redemption',
        'Contamination', 'MeaningMaking'
    ],
    "Self-Concept Theory": [
        'ActualSelf', 'IdealSelf', 'OughtSelf'
    ]
}


def _build_dataframe(scores: dict) -> pd.DataFrame:
    rows = []
    for model, constructs in MODEL_MAPPING.items():
        for con in constructs:
            rows.append({
                "Model": model,
                "Construct": con,
                "Score": scores.get(con, {}).get("CRS", 0.0)
            })
    return pd.DataFrame(rows)


def plot_model_construct_scores(scores: dict, *, display: bool = False):
    """Return a Plotly sunburst.  If display=True, also render inside Streamlit."""
    df = _build_dataframe(scores)
    fig = px.sunburst(
        df, path=['Model', 'Construct'], values='Score',
        color='Model', hover_data=['Score'],
        color_discrete_sequence=px.colors.qualitative.Set3,
        title="CRS distribution across identity theories"
    )
    if display:
        st.plotly_chart(fig, use_container_width=True, key="sunburst")
    return fig


def save_plot_as_image(scores: dict, filepath: str, scale: int = 2):
    """Write a high-resolution PNG using Plotly + Kaleido."""
    fig = plot_model_construct_scores(scores, display=False)
    pio.write_image(fig, filepath, format="png", scale=scale)
    return filepath

