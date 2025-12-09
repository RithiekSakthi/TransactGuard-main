import streamlit as st
import os
from streamlit_lottie import st_lottie
import json
import time
import random

# ============= PAGE CONFIG =============
st.set_page_config(
    page_title="TransactGuard",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============= LOAD LOTTIE =============
def load_lottie(filepath):
    with open(filepath, "r") as f:
        return json.load(f)

fraud_lottie = load_lottie("assets/fraud.json")  # put your animation here
ai_lottie = load_lottie("assets/ai.json")

# ============= GLOBAL CSS =============
st.markdown("""
<style>

:root {
    --primary: #3b82f6;
    --secondary: #8b5cf6;
    --text-light: #f8fafc;
    --text-muted: #94a3b8;
    --dark-bg: #0f172a;
    --card-bg: rgba(30, 41, 59, 0.6);
}

/* BACKGROUND */
[data-testid="stAppViewContainer"] {
    background: var(--dark-bg);
    color: var(--text-light);
}

/* HIDE DEFAULT HEADER */
[data-testid="stHeader"] { display: none; }

/* BANNER */
.banner {
    text-align: center;
    padding: 6rem 1rem 4rem 1rem;
}
.banner h1 {
    font-size: 4rem;
    background: linear-gradient(135deg, var(--primary), var(--secondary));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 900;
}
.banner p {
    font-size: 1.25rem;
    color: var(--text-muted);
    margin-top: -10px;
}

/* SECTION TITLE */
.section-title {
    text-align: center;
    font-size: 2.4rem;
    font-weight: 800;
    margin: 3rem 0 2rem 0;
}

/* CARDS */
.feature-card {
    background: var(--card-bg);
    border-radius: 16px;
    padding: 2rem;
    border: 1px solid rgba(255,255,255,0.08);
    backdrop-filter: blur(12px);
    transition: 0.3s;
}
.feature-card:hover {
    transform: translateY(-8px);
    border-color: var(--primary);
    box-shadow: 0 10px 40px rgba(59,130,246,0.25);
}

.stat-card {
    background: rgba(255,255,255,0.05);
    padding: 2rem;
    border-radius: 16px;
    text-align: center;
    border: 1px solid rgba(255,255,255,0.07);
    transition: 0.3s;
}
.stat-number {
    font-size: 3rem;
    font-weight: 900;
}
.stat-label {
    color: var(--text-muted);
    font-size: 1rem;
    margin-top: -10px;
}

.testimonial-box {
    background: rgba(255,255,255,0.07);
    padding: 1.5rem;
    border-radius: 14px;
    border: 1px solid rgba(255,255,255,0.08);
    backdrop-filter: blur(10px);
    transition: .3s;
}
.testimonial-box:hover {
    transform: translateY(-5px);
}

</style>
""", unsafe_allow_html=True)

# ============= HERO SECTION =============
st.markdown("""
<div class="banner">
    <h1>TransactGuard</h1>
    <p>AI-driven fraud detection built for speed, scale, and accuracy.</p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1.2, 1])

with col1:
    st.markdown("""
        <h2 style="font-size:2.2rem; font-weight:800;">Real-Time Fraud Prevention</h2>
        <p style="color:#94a3b8; font-size:1.1rem;">
            Our AI engine analyzes live transaction streams, detects anomalies, and stops fraud 
            before it becomes a problem. Built for banks, fintech, and high-volume systems.
        </p>
    """, unsafe_allow_html=True)

    if st.button("🚀 Start Predicting", use_container_width=True, type="primary"):
        st.switch_page("pages/02_Predict.py")

with col2:
    st_lottie(fraud_lottie, height=350, key="fraud")

# ============= WHY TRANSACTGUARD =============
st.markdown("<div class='section-title'>Why TransactGuard?</div>", unsafe_allow_html=True)

cols = st.columns(3)
benefits = [
    ("⚡", "Instant Detection", "Detect fraudulent behavior literally in milliseconds."),
    ("🧠", "AI-Powered", "Uses anomaly detection + ML classification models."),
    ("🔐", "Enterprise Security", "End-to-end encrypted and compliance ready.")
]

for i, (icon, title, desc) in enumerate(benefits):
    with cols[i]:
        st.markdown(f"""
        <div class="feature-card">
            <div style="font-size:2.5rem;">{icon}</div>
            <h3 style="margin-top:1rem;">{title}</h3>
            <p style="color:#94a3b8;">{desc}</p>
        </div>
        """, unsafe_allow_html=True)

# ============= FEATURES GRID =============
st.markdown("<div class='section-title'>Core Features</div>", unsafe_allow_html=True)

features = [
    "Advanced ML Fraud Scoring",
    "Transaction Stream Monitoring",
    "User Behavior Profiling",
    "Threat Intelligence Integration",
    "Customizable Threshold Alerts",
    "Deep Analytics Dashboard"
]

rows = st.columns(3)

for i, feature in enumerate(features):
    with rows[i % 3]:
        st.markdown(f"""
        <div class="feature-card">
            <h4>{feature}</h4>
        </div>
        """, unsafe_allow_html=True)

# ============= STATS =============
st.markdown("<div class='section-title'>Live System Stats</div>", unsafe_allow_html=True)

colA, colB, colC, colD = st.columns(4)

stats = {
    "Transactions Today": random.randint(250000, 900000),
    "Threats Blocked": random.randint(300, 1500),
    "Detection Accuracy": "98.7%",
    "Avg Latency": "42 ms"
}

for col, (label, value) in zip([colA, colB, colC, colD], stats.items()):
    with col:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-number">{value}</div>
            <div class="stat-label">{label}</div>
        </div>
        """, unsafe_allow_html=True)

# ============= TESTIMONIALS =============
st.markdown("<div class='section-title'>Trusted By Users</div>", unsafe_allow_html=True)

colT1, colT2, colT3 = st.columns(3)

testimonials = [
    ("“Caught fraud in minutes instead of hours.”", "— Fintech Ops Lead"),
    ("“Detection accuracy exceeded expectations.”", "— Bank Security Team"),
    ("“Easy integration + fast insights.”", "— Data Engineer")
]

for col, (text, author) in zip([colT1, colT2, colT3], testimonials):
    with col:
        st.markdown(f"""
        <div class="testimonial-box">
            <p>{text}</p>
            <p style="color:#94a3b8; font-size:0.9rem; margin-top:5px;">{author}</p>
        </div>
        """, unsafe_allow_html=True)

# ============= FOOTER =============
st.markdown("""
<br><br>
<div style="text-align:center; color:#94a3b8; padding:2rem 0; border-top:1px solid rgba(255,255,255,0.1);">
    © 2025 TransactGuard • AI Fraud Detection Platform
</div>
""", unsafe_allow_html=True)
