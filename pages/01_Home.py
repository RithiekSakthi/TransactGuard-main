import streamlit as st
import os

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Home - TransactGuard",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CUSTOM CSS & THEME INJECTION ---
st.markdown("""
<style>
    /* --- GLOBAL STREAMLIT OVERRIDES --- */
    [data-testid="stAppViewContainer"] {
        background-color: #0f172a; /* Dark Background */
        color: #f8fafc;
    }
    
    [data-testid="stHeader"] {
        background-color: rgba(0,0,0,0); /* Transparent Header */
        z-index: 1; /* Lower z-index so our menu sits on top */
    }
    
    /* HIDE STANDARD STREAMLIT SIDEBAR & MENU */
    [data-testid="stSidebar"], [data-testid="collapsedControl"] {
        display: none;
    }
    
    /* Remove standard sidebar padding for full immersion */
    .block-container {
        padding-top: 5rem; /* More padding top to clear the menu */
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

    /* --- FAB / CIRCULAR MENU STYLES --- */
    .fab-wrapper {
        position: fixed;
        top: 20px;    /* MOVED TO TOP */
        left: 20px;   /* MOVED TO LEFT */
        z-index: 99999;
    }
    
    .fab-button {
        width: 65px;
        height: 65px;
        background: var(--accent-gradient);
        border-radius: 50%;
        box-shadow: 0 10px 20px rgba(59, 130, 246, 0.4);
        display: flex;
        justify-content: center;
        align-items: center;
        position: relative;
        z-index: 20;
        cursor: pointer;
        transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }
    
    .fab-icon {
        font-size: 28px;
        color: white;
        transition: transform 0.3s ease;
        line-height: 1;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    
    /* Rotate on hover (optional for hamburger, but nice effect) */
    .fab-wrapper:hover .fab-button { transform: scale(1.1); }
    
    .fab-list {
        position: absolute;
        top: 0;
        left: 0;
        padding: 0;
        margin: 0;
        list-style: none;
        width: 65px;
        height: 65px;
        pointer-events: none;
    }
    
    /* INVISIBLE BRIDGE for Hover Stability (Top-Left Origin) */
    .fab-list::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 0;
        height: 0;
        border-radius: 0 0 100% 0; /* Quarter circle facing bottom-right */
        background: transparent;
        z-index: -1;
        transition: width 0.1s, height 0.1s;
    }
    
    .fab-wrapper:hover .fab-list::before {
        width: 300px;
        height: 300px;
    }
    
    .fab-item {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%); /* Start at center */
        width: 50px;
        height: 50px;
        border-radius: 50%;
        background: rgba(30, 41, 59, 0.9);
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(8px);
        display: flex;
        justify-content: center;
        align-items: center;
        text-decoration: none;
        font-size: 20px;
        opacity: 0;
        transition: all 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55);
        box-shadow: 0 5px 15px rgba(0,0,0,0.3);
        cursor: pointer;
    }
    
    .fab-item:hover {
        background: var(--primary-color);
        border-color: var(--primary-color);
        box-shadow: 0 0 15px var(--primary-color);
        z-index: 30;
    }
    
    /* Labels now appear to the RIGHT of the icons */
    .fab-label {
        position: absolute;
        left: 60px; /* Moved to Right side */
        background: #1e293b;
        color: white;
        padding: 5px 12px;
        border-radius: 6px;
        font-size: 13px;
        font-weight: 600;
        opacity: 0;
        visibility: hidden;
        transition: opacity 0.3s, transform 0.3s;
        white-space: nowrap;
        box-shadow: 0 4px 6px rgba(0,0,0,0.2);
        border: 1px solid rgba(255,255,255,0.1);
        transform: translateX(-10px);
        pointer-events: none;
    }
    
    .fab-item:hover .fab-label {
        opacity: 1;
        visibility: visible;
        transform: translateX(0);
    }
    
    .fab-wrapper:hover .fab-list { pointer-events: auto; }
    
    /* --- FAN OUT LOGIC (Top-Left to Bottom-Right) --- */
    
    /* Item 1: Home (Right) */
    .fab-wrapper:hover .fab-item:nth-child(1) {
        transform: translate(120px, -50%);
        opacity: 1;
        transition-delay: 0.05s;
    }
    /* Item 2: Predict */
    .fab-wrapper:hover .fab-item:nth-child(2) {
        transform: translate(100px, 40px);
        opacity: 1;
        transition-delay: 0.08s;
    }
    /* Item 3: Results */
    .fab-wrapper:hover .fab-item:nth-child(3) {
        transform: translate(60px, 90px);
        opacity: 1;
        transition-delay: 0.11s;
    }
    /* Item 4: Data */
    .fab-wrapper:hover .fab-item:nth-child(4) {
        transform: translate(10px, 130px);
        opacity: 1;
        transition-delay: 0.14s;
    }
    /* Item 5: About (Down) */
    .fab-wrapper:hover .fab-item:nth-child(5) {
        transform: translate(-50%, 160px);
        opacity: 1;
        transition-delay: 0.17s;
    }

    /* --- CARD STYLES --- */
    .hero-container {
        text-align: center;
        padding: 2rem 0 2rem;
        animation: fadeIn 1s ease-in;
    }
    
    .hero-title {
        font-size: 3.5rem;
        font-weight: 800;
        background: var(--accent-gradient);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1rem;
        line-height: 1.2;
    }
    
    .custom-card {
        background-color: var(--card-bg);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 2rem;
        text-align: center;
        transition: transform 0.3s ease, border-color 0.3s ease, box-shadow 0.3s ease;
        height: 100%;
        min-height: 250px;
        backdrop-filter: blur(10px);
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: flex-start;
    }
    
    .custom-card:hover {
        transform: translateY(-5px);
        border-color: var(--primary-color);
        box-shadow: 0 10px 30px -10px rgba(59, 130, 246, 0.3);
    }

    .process-card {
        border-top: 4px solid var(--primary-color);
    }
    
    h1, h2, h3, p { font-family: 'Inter', sans-serif !important; }
    
    @keyframes fadeIn { 
        from { opacity: 0; transform: translateY(20px); } 
        to { opacity: 1; transform: translateY(0); } 
    }
</style>
""", unsafe_allow_html=True)

# --- INJECT MENU ---
# Added items: Home, Predict, Results, Data, About
# Changed Icon to Hamburger (☰)
st.markdown("""
    <div class="fab-wrapper">
        <div class="fab-button">
            <span class="fab-icon">☰</span>
        </div>
        <ul class="fab-list">
            <a href="/" target="_self" class="fab-item">
                🏠
                <span class="fab-label">Home</span>
            </a>
            <a href="Predict" target="_self" class="fab-item">
                🚀
                <span class="fab-label">Predict</span>
            </a>
            <a href="Results" target="_self" class="fab-item">
                📈
                <span class="fab-label">Results</span>
            </a>
            <a href="Data" target="_self" class="fab-item">
                💾
                <span class="fab-label">Data</span>
            </a>
             <a href="About" target="_self" class="fab-item">
                ℹ️
                <span class="fab-label">About</span>
            </a>
        </ul>
    </div>
""", unsafe_allow_html=True)

# --- BANNER ---
# Display banner if file exists, otherwise show a styled placeholder
# This prevents errors if 'assets/images/logo.png' is missing in your local environment
if os.path.exists("assets/images/logo.png"):
    st.image("assets/images/logo.png", use_container_width=True)
else:
    # Fallback banner visualization
    st.markdown("""
        <div style="
            width: 100%; 
            height: 200px; 
            background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); 
            border-radius: 12px; 
            display: flex; 
            align-items: center; 
            justify-content: center;
            border: 1px solid rgba(255,255,255,0.05);
            margin-bottom: 2rem;">
            <div style="text-align: center;">
                <h1 style="font-size: 3rem; margin:0;">🛡️ TransactGuard</h1>
                <p style="color: #94a3b8;">Secure Transaction Monitoring</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

# --- HERO SECTION ---
st.markdown("""
<div class="hero-container">
    <h1 class="hero-title">Fraud Transaction Prediction</h1>
    <p style="font-size: 1.1rem; color: #94a3b8; max-width: 600px; margin: 0 auto 2rem auto;">
        Predict fraudulent transactions with precision and confidence. Our advanced algorithms analyze transaction data in real-time.
    </p>
</div>
""", unsafe_allow_html=True)

# --- BUTTON ---
col1, col2, col3 = st.columns([3, 1, 3])
with col2:
    if st.button("🚀 Get Started", use_container_width=True, type="primary"):
        st.switch_page("pages/02_Predict.py")

# --- FRAUD TYPES ---
st.markdown('<h2 style="text-align: center; margin: 3rem 0 2rem; font-weight: 700;">Real-Life Fraud Transactions</h2>', unsafe_allow_html=True)

fraud_types = [
    ("💳", "Unauthorized Credit Card Use", "A credit card was used without owner consent."),
    ("🎣", "Phishing Scams", "User tricked into providing sensitive information."),
    ("🔓", "Account Takeover", "Attacker gained control of user account."),
    ("🙋", "Identity Theft", "Personal information stolen and used for fraud.")
]

cols = st.columns(4)
for i, (icon, title, desc) in enumerate(fraud_types):
    with cols[i]:
        st.markdown(f"""
        <div class="custom-card">
            <div style="font-size: 3rem; margin-bottom: 1rem;">{icon}</div>
            <div style="font-size: 1.1rem; font-weight: 700; margin-bottom: 0.75rem; color: #f8fafc;">{title}</div>
            <div style="font-size: 0.9rem; color: #94a3b8;">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

# --- PROCESS SECTION ---
st.markdown('<h2 style="text-align: center; margin: 4rem 0 2rem; font-weight: 700;">Our Process</h2>', unsafe_allow_html=True)

steps = [
    ("📥", "Data Collection", "Gather transaction data from various sources."),
    ("🔍", "Analysis and Prediction", "Analyze patterns and predict fraud."),
    ("📊", "Insights", "Provide insights on fraud prevention.")
]

cols_steps = st.columns(3)
for i, (icon, title, desc) in enumerate(steps):
    with cols_steps[i]:
        st.markdown(f"""
        <div class="custom-card process-card">
            <div style="font-size: 3rem; margin-bottom: 1rem;">{icon}</div>
            <div style="font-size: 1.25rem; font-weight: 700; margin-bottom: 0.75rem; color: #f8fafc;">{title}</div>
            <div style="font-size: 0.95rem; color: #94a3b8;">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("""
<div style="margin-top: 4rem; padding: 2rem 0; border-top: 1px solid rgba(255,255,255,0.1); text-align: center; color: #94a3b8;">
    <p>Built with Streamlit & Machine Learning • © 2025 TransactGuard</p>
</div>
""", unsafe_allow_html=True)
