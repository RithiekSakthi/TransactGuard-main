import streamlit as st
import os
import base64

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Home - TransactGuard",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- HELPER FUNCTION FOR VIDEO BACKGROUND ---
def get_video_html(video_path):
    """
    Reads a local video file and returns a base64 encoded HTML string 
    to be used as a background.
    """
    if not os.path.exists(video_path):
        return f"""
        <style>
        [data-testid="stAppViewContainer"] {{
            background-color: #0f172a;
        }}
        </style>
        <div style="position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%); color: white; z-index: 9999;">
            ⚠️ Video file not found: {video_path}<br>
            Please ensure the file is in the same directory.
        </div>
        """
        
    with open(video_path, "rb") as f:
        video_bytes = f.read()
    
    encoded_video = base64.b64encode(video_bytes).decode()
    
    return f"""
    <video autoplay muted loop id="myVideo">
        <source src="data:video/mp4;base64,{encoded_video}" type="video/mp4">
        Your browser does not support HTML5 video.
    </video>
    <script>
        const video = document.getElementById('myVideo');
        if (video) {{
            video.playbackRate = 0.75;
        }}
    </script>
    """

# --- CUSTOM CSS & THEME INJECTION ---
st.markdown("""
<style>
    /* --- GLOBAL STREAMLIT OVERRIDES --- */
    [data-testid="stAppViewContainer"] {
        background-color: transparent; /* Transparent to show video */
        color: #f8fafc;
    }
    
    [data-testid="stHeader"] {
        display: none; /* Hide default Streamlit header */
    }
    
    [data-testid="stSidebar"], [data-testid="collapsedControl"] {
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

    /* --- VIDEO BACKGROUND --- */
    #myVideo {
        position: fixed;
        right: 0;
        bottom: 0;
        min-width: 100%; 
        min-height: 100%;
        z-index: -1;
        opacity: 0.75; /* Transparency 75% */
        object-fit: cover;
    }

    /* --- FAB / CIRCULAR MENU STYLES --- */
    .fab-wrapper {
        position: fixed;
        top: 30px;
        left: 30px;   
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
    
    .fab-list::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 0;
        height: 0;
        border-radius: 0 0 100% 0;
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
        transform: translate(-50%, -50%);
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
    
    .fab-label {
        position: absolute;
        left: 60px;
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
    
    .fab-wrapper:hover .fab-item:nth-child(1) { transform: translate(150px, -50%); opacity: 1; transition-delay: 0.05s; }
    .fab-wrapper:hover .fab-item:nth-child(2) { transform: translate(135px, 55px); opacity: 1; transition-delay: 0.08s; }
    .fab-wrapper:hover .fab-item:nth-child(3) { transform: translate(100px, 100px); opacity: 1; transition-delay: 0.11s; }
    .fab-wrapper:hover .fab-item:nth-child(4) { transform: translate(55px, 135px); opacity: 1; transition-delay: 0.14s; }
    .fab-wrapper:hover .fab-item:nth-child(5) { transform: translate(-50%, 150px); opacity: 1; transition-delay: 0.17s; }

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
    
    /* --- NEW FIXED BANNER STYLES --- */
    .banner-container {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 180px;
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.95) 0%, rgba(30, 41, 59, 0.95) 100%);
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
        backdrop-filter: blur(15px);
        z-index: 99990;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }
    
    .banner-title {
        font-size: 3.5rem;
        font-weight: 800;
        color: #ffffff;
        margin: 0;
        letter-spacing: 2px;
        animation: glow 3s ease-in-out infinite alternate;
    }
    
    .banner-subtitle {
        font-size: 1.2rem;
        color: #94a3b8;
        margin-top: 0.2rem;
        font-weight: 400;
        letter-spacing: 4px;
        text-transform: uppercase;
    }

    @keyframes glow {
        from { text-shadow: 0 0 10px rgba(59, 130, 246, 0.5); }
        to { text-shadow: 0 0 20px rgba(59, 130, 246, 0.8), 0 0 30px rgba(139, 92, 246, 0.6); }
    }
    
    h1, h2, h3, p { font-family: 'Inter', sans-serif !important; }
    
    @keyframes fadeIn { 
        from { opacity: 0; transform: translateY(20px); } 
        to { opacity: 1; transform: translateY(0); } 
    }
</style>
""", unsafe_allow_html=True)

# --- VIDEO INJECTION WITH BASE64 ---
video_file_name = "0_Global_Market_Financial_Data_3840x2160.mp4"
st.markdown(get_video_html(video_file_name), unsafe_allow_html=True)

# --- INJECT MENU ---
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
                🗃️
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
st.markdown("""
    <div class="banner-container">
        <h1 class="banner-title">Transact Guard</h1>
        <p class="banner-subtitle">Fraud Detection</p>
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
