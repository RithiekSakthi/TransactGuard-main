import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="About - TransactGuard",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CUSTOM CSS & THEME INJECTION ---
st.markdown("""
<style>
    /* --- GLOBAL STREAMLIT OVERRIDES --- */
    [data-testid="stAppViewContainer"] {
        background-color: #0f172a; 
        color: #f8fafc;
    }
    [data-testid="stHeader"], [data-testid="stSidebar"], [data-testid="collapsedControl"] {
        display: none;
    }
    .block-container {
        padding-top: 220px;
        padding-bottom: 5rem;
    }

    /* --- GLOBAL VARIABLES --- */
    :root {
        --primary-color: #3b82f6;
        --background-dark: #0f172a;
        --card-bg: rgba(30, 41, 59, 0.7);
        --text-primary: #f8fafc;
        --text-secondary: #94a3b8;
        --accent-gradient: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%);
    }

    /* --- MENU STYLES --- */
    .fab-wrapper { position: fixed; top: 30px; left: 30px; z-index: 99999; }
    .fab-button {
        width: 65px; height: 65px; background: var(--accent-gradient);
        border-radius: 50%; box-shadow: 0 10px 20px rgba(59, 130, 246, 0.4);
        display: flex; justify-content: center; align-items: center;
        transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }
    .fab-icon { font-size: 28px; color: white; }
    .fab-wrapper:hover .fab-button { transform: scale(1.1); }
    .fab-list {
        position: absolute; top: 0; left: 0; padding: 0; margin: 0; list-style: none;
        width: 65px; height: 65px; pointer-events: none;
    }
    .fab-list::before {
        content: ''; position: absolute; top: 0; left: 0; width: 0; height: 0;
        border-radius: 0 0 100% 0; background: transparent; z-index: -1;
        transition: width 0.1s, height 0.1s;
    }
    .fab-wrapper:hover .fab-list::before { width: 300px; height: 300px; }
    .fab-item {
        position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);
        width: 50px; height: 50px; border-radius: 50%;
        background: rgba(30, 41, 59, 0.9); border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(8px); display: flex; justify-content: center; align-items: center;
        text-decoration: none; font-size: 20px; opacity: 0;
        transition: all 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55);
        box-shadow: 0 5px 15px rgba(0,0,0,0.3);
    }
    .fab-item:hover { background: var(--primary-color); z-index: 30; }
    .fab-label {
        position: absolute; left: 60px; background: #1e293b; color: white;
        padding: 5px 12px; border-radius: 6px; font-size: 13px; font-weight: 600;
        opacity: 0; visibility: hidden; transition: opacity 0.3s, transform 0.3s;
        white-space: nowrap; pointer-events: none; transform: translateX(-10px);
    }
    .fab-item:hover .fab-label { opacity: 1; visibility: visible; transform: translateX(0); }
    .fab-wrapper:hover .fab-list { pointer-events: auto; }
    .fab-wrapper:hover .fab-item:nth-child(1) { transform: translate(150px, -50%); opacity: 1; transition-delay: 0.05s; }
    .fab-wrapper:hover .fab-item:nth-child(2) { transform: translate(135px, 55px); opacity: 1; transition-delay: 0.08s; }
    .fab-wrapper:hover .fab-item:nth-child(3) { transform: translate(100px, 100px); opacity: 1; transition-delay: 0.11s; }
    .fab-wrapper:hover .fab-item:nth-child(4) { transform: translate(55px, 135px); opacity: 1; transition-delay: 0.14s; }
    .fab-wrapper:hover .fab-item:nth-child(5) { transform: translate(-50%, 150px); opacity: 1; transition-delay: 0.17s; }

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

    /* --- ABOUT SPECIFIC STYLES --- */
    .card {
        background-color: var(--card-bg);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        backdrop-filter: blur(10px);
    }
    .section-title {
        color: var(--text-primary);
        font-size: 24px;
        font-weight: 700;
        margin: 2rem 0 1rem 0;
        border-left: 4px solid var(--primary-color);
        padding-left: 1rem;
    }
    h1, h2, h3, p, strong { font-family: 'Inter', sans-serif !important; }
</style>
""", unsafe_allow_html=True)

# --- INJECT MENU ---
st.markdown("""
    <div class="fab-wrapper">
        <div class="fab-button"><span class="fab-icon">☰</span></div>
        <ul class="fab-list">
            <a href="/" target="_self" class="fab-item">🏠<span class="fab-label">Home</span></a>
            <a href="Predict" target="_self" class="fab-item">🚀<span class="fab-label">Predict</span></a>
            <a href="Results" target="_self" class="fab-item">📈<span class="fab-label">Results</span></a>
            <a href="Data" target="_self" class="fab-item">🗃️<span class="fab-label">Data</span></a>
            <a href="About" target="_self" class="fab-item">ℹ️<span class="fab-label">About</span></a>
        </ul>
    </div>
""", unsafe_allow_html=True)

# --- BANNER ---
st.markdown("""
    <div class="banner-container">
        <h1 class="banner-title">Transact Guard</h1>
        <p class="banner-subtitle">Fraud Detection</p>
    </div>
""", unsafe_allow_html=True)

# --- PAGE CONTENT ---

st.markdown('<h1 class="section-title" style="font-size: 32px; border: none; text-align: center;">About Us</h1>', unsafe_allow_html=True)

st.markdown('<h2 class="section-title">Who We Are</h2>', unsafe_allow_html=True)
st.markdown('<div class="card">We are Freshbuilders, AI students from SAIT. We developed TransactGuard to detect fraud in transactions using machine learning.</div>', unsafe_allow_html=True)

st.markdown('<h2 class="section-title">Meet The Team</h2>', unsafe_allow_html=True)
team = [
    ("Dany", "Project Coordinator and UI Designer"),
    ("Nay", "Technical Lead and Developer"),
    ("Ohm", "Deployment Lead"),
    ("Rithiek", "ML Integration Lead"),
    ("Angel", "Testing and Documentation Lead")
]

cols = st.columns(2)
for idx, (name, role) in enumerate(team):
    with cols[idx % 2]:
        st.markdown(f'''
            <div class="card" style="display: flex; align-items: center; border-left: 3px solid var(--primary-color);">
                <div style="font-size: 1.5rem; margin-right: 1rem;">👤</div>
                <div>
                    <div style="font-weight: 700; color: white;">{name}</div>
                    <div style="color: var(--text-secondary); font-size: 0.9rem;">{role}</div>
                </div>
            </div>
        ''', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown('<h2 class="section-title">Strengths</h2>', unsafe_allow_html=True)
    st.markdown('<div class="card" style="height: 150px; display: flex; align-items: center;">10+ years combined experience • Technical diversity • Data analysis expertise • Fresh ideas</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<h2 class="section-title">Challenges & Solutions</h2>', unsafe_allow_html=True)
    st.markdown('<div class="card" style="height: 150px; display: flex; align-items: center;">Limited ML experience • Diverse backgrounds • Mentorship & pair programming support</div>', unsafe_allow_html=True)

st.markdown('<h2 class="section-title">Our Work Philosophy</h2>', unsafe_allow_html=True)
st.markdown('<div class="card" style="text-align: center; font-size: 1.2rem; font-weight: 600;">We value collaboration, learning, and mutual support.</div>', unsafe_allow_html=True)
