"""About page"""
import streamlit as st
from src.styles import apply_dark_theme, render_sidebar

st.set_page_config(page_title="About - TransactGuard", layout="wide", initial_sidebar_state="expanded")
apply_dark_theme()
render_sidebar()

# --- ADDITIONAL CUSTOM CSS FOR ENHANCED STYLING ---
st.markdown("""
<style>
    /* --- BANNER STYLES --- */
    .banner-container {
        position: fixed; top: 0; left: 0; width: 100%; height: 180px;
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.95) 0%, rgba(30, 41, 59, 0.95) 100%);
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
        backdrop-filter: blur(15px); z-index: 99990;
        display: flex; flex-direction: column; align-items: center; justify-content: center;
    }
    .banner-title {
        font-size: 3.5rem; font-weight: 800; color: #ffffff; margin: 0;
        letter-spacing: 2px; animation: glow 3s ease-in-out infinite alternate;
    }
    .banner-subtitle {
        font-size: 1.2rem; color: #94a3b8; margin-top: 0.2rem;
        font-weight: 400; letter-spacing: 4px; text-transform: uppercase;
    }
    @keyframes glow {
        from { text-shadow: 0 0 10px rgba(59, 130, 246, 0.5); }
        to { text-shadow: 0 0 20px rgba(59, 130, 246, 0.8), 0 0 30px rgba(139, 92, 246, 0.6); }
    }

    /* --- CARD ENHANCEMENTS --- */
    .card {
        background-color: rgba(30, 41, 59, 0.7);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        backdrop-filter: blur(10px);
    }
    
    /* --- SECTION TITLE ENHANCEMENTS --- */
    .section-title {
        color: #f8fafc;
        font-size: 24px;
        font-weight: 700;
        margin: 2rem 0 1rem 0;
        border-left: 4px solid #3b82f6;
        padding-left: 1rem;
    }
    
    h1, h2, h3, p, strong, li { font-family: 'Inter', sans-serif !important; }
</style>
""", unsafe_allow_html=True)

# --- BANNER ---
st.markdown("""
    <div class="banner-container">
        <h1 class="banner-title">Transact Guard</h1>
        <p class="banner-subtitle">Fraud Detection</p>
    </div>
""", unsafe_allow_html=True)

# Add padding to account for fixed banner
st.markdown('<div style="height: 200px;"></div>', unsafe_allow_html=True)

# --- PAGE CONTENT ---
st.markdown('<h1 class="section-title" style="font-size: 36px;">About Us</h1>', unsafe_allow_html=True)

st.markdown('<h2 class="section-title">Who We Are</h2>', unsafe_allow_html=True)
st.markdown("""
<div class="card">
We are TransactGuard, a dynamic team of AI students from the Southern Alberta Institute of Technology (SAIT).<br><br>
United by a passion for financial security and machine learning, we developed TransactGuard—a cutting-edge solution designed to detect fraudulent transactions. Our mission is to leverage advanced algorithms to build a safer digital economy.
</div>
""", unsafe_allow_html=True)

team = [
    ("Dany", "Project Coordinator and UI Designer"),
    ("Nay", "Technical Lead and Developer"),
    ("Ohm", "Deployment Lead"),
    ("Rithiek", "ML Integration Lead"),
    ("Angel", "Testing and Documentation Lead")
]

col_left, col_right = st.columns([1.2, 1], gap="large")
with col_left:
    st.markdown('<h2 class="section-title">Meet The Team</h2>', unsafe_allow_html=True)
    for name, role in team:
        st.markdown(f'''
            <div class="card" style="display: flex; align-items: center; border-left: 3px solid #3b82f6;">
                <div style="font-size: 1.5rem; margin-right: 1rem;">👤</div>
                <div>
                    <div style="font-weight: 700; color: white;">{name}</div>
                    <div style="color: #94a3b8; font-size: 0.9rem;">{role}</div>
                </div>
            </div>
        ''', unsafe_allow_html=True)

with col_right:
    st.image("assets/images/team_photo.jpg", width=360)

st.markdown('<h2 class="section-title">Strengths</h2>', unsafe_allow_html=True)
st.markdown("""
<div class="card">
<ul style="margin: 0 0 0 18px; padding: 0; color: #f8fafc;">
  <li>10+ years combined experience</li>
  <li>Technical diversity</li>
  <li>Data analysis expertise</li>
  <li>Fresh ideas</li>
</ul>
</div>
""", unsafe_allow_html=True)

st.markdown('<h2 class="section-title">Our Work Philosophy</h2>', unsafe_allow_html=True)
st.markdown('<div class="card">We value collaboration, learning, and mutual support.</div>', unsafe_allow_html=True)
