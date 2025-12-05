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
            background-color: #0f172a !important;
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
    <div class="video-bg">
        <video autoplay muted loop playsinline>
            <source src="data:video/mp4;base64,{encoded_video}" type="video/mp4">
        </video>
    </div>

    <style>
    .video-bg {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        overflow: hidden;
        z-index: -1;
    }}
    
    .video-bg video {{
        position: absolute;
        top: 50%;
        left: 50%;
        min-width: 100%;
        min-height: 100%;
        width: auto;
        height: auto;
        transform: translate(-50%, -50%);
        object-fit: cover;
        opacity: 0.75;
    }}

    /* FORCE STREAMLIT TRANSPARENCY */
    body, [data-testid="stAppViewContainer"], [data-testid="stMain"] {{
        background: transparent !important;
    }}

    /* FIX WHITE FLASH ON LOAD */
    html, body {{
        height: 100%;
        overflow-x: hidden;
    }}
    </style>

    <script>
        const vid = document.querySelector(".video-bg video");
        if (vid) {{
            vid.playbackRate = 0.75;
        }}
    </script>
    """

# --- CUSTOM CSS & THEME INJECTION ---
st.markdown("""
<style>
    /* GLOBAL OVERRIDES */
    [data-testid="stHeader"] { display: none; }
    [data-testid="stSidebar"], [data-testid="collapsedControl"] { display: none; }

    .block-container {
        padding-top: 220px;
        padding-bottom: 5rem;
    }

    :root {
        --primary-color: #3b82f6;
        --background-dark: #0f172a;
        --card-bg: rgba(30, 41, 59, 0.7);
        --text-primary: #f8fafc;
        --text-secondary: #94a3b8;
        --accent-gradient: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%);
    }

    /* FAB + OTHER CSS HERE… (unchanged) */
</style>
""", unsafe_allow_html=True)

# --- VIDEO INJECTION WITH BASE64 ---
video_file_name = "assets/images/0_Global_Market_Financial_Data_3840x2160.mp4"
st.markdown(get_video_html(video_file_name), unsafe_allow_html=True)

# --- INJECT MENU ---
st.markdown("""
    <div class="fab-wrapper">
        <div class="fab-button"><span class="fab-icon">☰</span></div>
        <ul class="fab-list">
            <a href="/" class="fab-item">🏠<span class="fab-label">Home</span></a>
            <a href="Predict" class="fab-item">🚀<span class="fab-label">Predict</span></a>
            <a href="Results" class="fab-item">📈<span class="fab-label">Results</span></a>
            <a href="Data" class="fab-item">🗃️<span class="fab-label">Data</span></a>
            <a href="About" class="fab-item">ℹ️<span class="fab-label">About</span></a>
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

# --- FOOTER ---
st.markdown("""
<div style="margin-top: 4rem; padding: 2rem 0; border-top: 1px solid rgba(255,255,255,0.1); text-align: center; color: #94a3b8;">
    <p>Built with Streamlit & Machine Learning • © 2025 TransactGuard</p>
</div>
""", unsafe_allow_html=True)
