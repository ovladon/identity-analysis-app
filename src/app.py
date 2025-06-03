"""
app.py  –  Streamlit front-end for Computational Identity Analysis
✓ Handles >1 M-char inputs (chunked pre-processing)
✓ Always-visible STOP button
✓ Run history via SQLite
✓ Source name in filenames
"""

import os, re, json, sqlite3, datetime, pathlib
import streamlit as st

from constructs import construct_objects
from preprocessing import preprocess_text
from file_processing import extract_text_from_file, extract_text_from_url
from temporal_weighting import weight_crs_by_age
from visualization import plot_model_construct_scores, save_plot_as_image
import theory_definitions

# ╭───────────────────────────  CONFIG  ───────────────────────────╮
MODEL_MAPPING = {
    "Erikson's Psychosocial Development": [
        'TrustVsMistrust','AutonomyVsShameDoubt','InitiativeVsGuilt',
        'IndustryVsInferiority','IdentityVsRoleConfusion',
        'IntimacyVsIsolation','GenerativityVsStagnation',
        'EgoIntegrityVsDespair'
    ],
    "Marcia's Identity Status Theory": [
        'IdentityAchievement','IdentityMoratorium',
        'IdentityForeclosure','IdentityDiffusion'
    ],
    "Social Identity Theory": [
        'InGroupIdentification','OutGroupDifferentiation',
        'PositiveDistinctiveness'
    ],
    "Narrative Identity Theory": [
        'Agency','Communion','Redemption','Contamination','MeaningMaking'
    ],
    "Self-Concept Theory": [
        'ActualSelf','IdealSelf','OughtSelf'
    ]
}
ALL_CONSTRUCTS = {c for lst in MODEL_MAPPING.values() for c in lst}

# ╭───────────────────────────  DB  ───────────────────────────────╮
conn = sqlite3.connect("runs.db")
conn.execute("""CREATE TABLE IF NOT EXISTS runs(
      id INTEGER PRIMARY KEY,
      ts TEXT, source TEXT, json_path TEXT, png_path TEXT
)""")
conn.commit()

# ╭───────────────────  helper functions  ─────────────────────────╮
def calculate_scores(text):
    out, bar = {}, st.progress(0)
    for i, (name, det) in enumerate(construct_objects.items(), 1):
        if st.session_state.get("stop"): break
        try:
            out.update(det.analyze_text(text))
        except Exception as e:
            out[name] = {"CRS": 0.0, "error": str(e)}
        bar.progress(i / len(construct_objects))
    return out

def ensure_keys(cs):
    for c in ALL_CONSTRUCTS:
        cs.setdefault(c, {"CRS": 0.0})

def model_means(cs):
    return {m: sum(cs[c]['CRS'] for c in lst)/len(lst)
            for m,lst in MODEL_MAPPING.items()}

def doi(model):
    any_c = next(iter(theory_definitions.theory_definitions[model]['constructs'].values()))
    return any_c.get('doi','N/A')

def interp(construct, score):
    d = theory_definitions.find_construct_description(construct)
    hi = d.get("high_interpretation", "high"); lo = d.get("low_interpretation", "low")
    if score >= 60: return f"High – {hi}"
    if score <= 30: return f"Low – {lo}"
    return f"Moderate – between high ({hi}) and low ({lo}) benchmarks"

def export_run(cs, ms, cint, mint, source_name):
    ts   = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    base = re.sub(r'\W+', '_', source_name)[:40] or "pasted_text"
    out_dir = pathlib.Path("exports"); out_dir.mkdir(exist_ok=True)
    json_path = out_dir / f"{base}_{ts}.json"
    png_path  = out_dir / f"{base}_{ts}.png"
    save_plot_as_image(cs, png_path)
    with open(json_path, "w") as fp:
        json.dump({
            "construct_scores": cs,
            "construct_interpretations": cint,
            "model_scores": ms,
            "model_interpretations": mint,
            "graph_path": str(png_path)
        }, fp, indent=2)
    conn.execute("INSERT INTO runs(ts,source,json_path,png_path) VALUES (?,?,?,?)",
                 (ts, base, str(json_path), str(png_path)))
    conn.commit()
    return json_path

# ╭─────────────────────  Streamlit UI  ───────────────────────────╮
st.set_page_config("Identity Analyzer", layout="wide")
st.title("Computational Identity Analyzer")

# STOP button (always visible)
if st.sidebar.button("STOP analysis"):
    st.session_state["stop"] = True
else:
    st.session_state.setdefault("stop", False)

# Run history
runs = conn.execute("SELECT id,ts,source,json_path FROM runs ORDER BY id DESC").fetchall()
if runs:
    sel = st.sidebar.selectbox("Run history", runs,
                               format_func=lambda r: f"{r[1]} — {r[2]}")
    if sel:
        st.sidebar.download_button("Download JSON",
                                   open(sel[3], "rb"),
                                   file_name=os.path.basename(sel[3]))

# Input source
mode = st.sidebar.radio("Input", ["Paste", "Upload", "URL"])
raw_text, source_name = "", "pasted_text"
if mode == "Paste":
    raw_text = st.text_area("Paste narrative text:", height=300)
elif mode == "Upload":
    up = st.file_uploader("Upload .txt / .pdf / .docx")
    if up:
        raw_text   = extract_text_from_file(up)
        source_name = up.name
else:
    url = st.text_input("URL")
    if url:
        raw_text   = extract_text_from_url(url)
        source_name = url

# Run analysis
if st.button("Analyse", disabled=not raw_text.strip()):
    st.session_state["stop"] = False

    clean = preprocess_text(raw_text)
    if st.session_state["stop"]: st.warning("Stopped."); st.stop()

    cs = calculate_scores(clean)
    ensure_keys(cs)
    cs = weight_crs_by_age(raw_text, cs)
    if st.session_state["stop"]: st.warning("Stopped."); st.stop()

    ms   = model_means(cs)
    cint = {c: interp(c, d['CRS']) for c, d in cs.items()}
    mint = {m: f"{theory_definitions.theory_definitions[m]['description']} (DOI {doi(m)})"
            for m in MODEL_MAPPING}

    st.header("Model overview")
    for m, avg in sorted(ms.items(), key=lambda x: x[1], reverse=True):
        st.subheader(f"{m} — avg CRS {avg:.1f}")
        st.write(mint[m])

    st.header("Construct details")
    for c, d in sorted(cs.items(), key=lambda x: x[1]['CRS'], reverse=True):
        st.markdown(f"**{c}** — {d['CRS']:.1f}")
        st.caption(cint[c])

    fig = plot_model_construct_scores(cs)
    st.plotly_chart(fig, use_container_width=True, key="sunburst")

    jpath = export_run(cs, ms, cint, mint, source_name)
    st.success(f"Saved {jpath}")

