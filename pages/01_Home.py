import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Home - TransactGuard",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CUSTOM CSS & THEME INJECTION ---
# This block injects the specific styles from your HTML file into the Streamlit app.
st.markdown("""
<style>
    /* --- GLOBAL STREAMLIT OVERRIDES --- */
    [data-testid="stAppViewContainer"] {
        background-color: #0f172a; /* Dark Background */
        color: #f8fafc;
    }
    
    [data-testid="stHeader"] {
        background-color: rgba(0,0,0,0); /* Transparent Header */
    }
    
    /* Remove standard sidebar padding for full immersion */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 5rem;
    }

    /* --- GLOBAL VARIABLES (From HTML) --- */
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
        bottom: 40px;
        right: 40px;
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
        font-size: 32px;
        color: white;
        transition: transform 0.3s ease;
        line-height: 1;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    
    .fab-wrapper:hover .fab-button { transform: scale(1.1); }
    .fab-wrapper:hover .fab-icon { transform: rotate(45deg); }
    
    .fab-list {
        position: absolute;
        bottom: 0;
        right: 0;
        padding: 0;
        margin: 0;
        list-style: none;
        width: 65px;
        height: 65px;
        pointer-events: none;
    }
    
    /* INVISIBLE BRIDGE for Hover Stability */
    .fab-list::before {
        content: '';
        position: absolute;
        bottom: 0;
        right: 0;
        width: 0;
        height: 0;
        border-radius: 100% 0 0 0;
        background: transparent;
        z-index: -1;
        transition: width 0.1s, height 0.1s;
    }
    
    .fab-wrapper:hover .fab-list::before {
        width: 250px;
        height: 250px;
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
        font-size: 22px;
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
        right: 60px;
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
        transform: translateX(10px);
        pointer-events: none;
    }
    
    .fab-item:hover .fab-label {
        opacity: 1;
        visibility: visible;
        transform: translateX(0);
    }
    
    .fab-wrapper:hover .fab-list { pointer-events: auto; }
    
    .fab-wrapper:hover .fab-item:nth-child(1) {
        transform: translate(-50%, -150px);
        opacity: 1;
        transition-delay: 0.05s;
    }
    .fab-wrapper:hover .fab-item:nth-child(2) {
        transform: translate(-120px, -120px);
        opacity: 1;
        transition-delay: 0.1s;
    }
    .fab-wrapper:hover .fab-item:nth-child(3) {
        transform: translate(-150px, -50%);
        opacity: 1;
        transition-delay: 0.15s;
    }

    /* --- COMPONENT STYLES --- */
    .hero-container {
        text-align: center;
        padding: 4rem 0 2rem;
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
        height: 100%; /* Ensure full height in columns */
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
    
    /* Animation */
    @keyframes fadeIn { 
        from { opacity: 0; transform: translateY(20px); } 
        to { opacity: 1; transform: translateY(0); } 
    }
</style>
""", unsafe_allow_html=True)

# --- INJECT HTML COMPONENTS ---

# 1. The Floating Action Button (FAB) Menu
# NOTE: Links in Streamlit usually require standard anchors. 
# Relative paths like "Predict" or "pages/02_Predict.py" depend on your setup.
st.markdown("""
    <div class="fab-wrapper">
        <div class="fab-button">
            <span class="fab-icon">+</span>
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
            <a href="Analytics" target="_self" class="fab-item">
                📊
                <span class="fab-label">Analytics</span>
            </a>
        </ul>
    </div>
""", unsafe_allow_html=True)

# 2. Hero Section
st.markdown("""
    <div class="hero-container">
        <div style="font-size: 4rem; margin-bottom: 1rem;">🛡️</div>
        <h1 class="hero-title">TransactGuard AI</h1>
        <p style="font-size: 1.2rem; color: #94a3b8; max-width: 700px; margin: 0 auto 2rem auto;">
            Next-generation financial security powered by machine learning. 
            Detect anomalies, prevent fraud, and secure transactions in real-time with 99.8% accuracy.
        </p>
    </div>
""", unsafe_allow_html=True)

# 3. Call to Action Button (Native Streamlit for logic)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    # Centered button with native Streamlit logic
    if st.button("🚀 Launch Prediction Engine", use_container_width=True, type="primary"):
        st.switch_page("pages/02_Predict.py")

st.markdown("---")

# 4. Fraud Types Section (Using HTML Cards for styling)
st.markdown('<h2 style="text-align: center; margin: 3rem 0 2rem; font-weight: 700;">Real-World Threat Detection</h2>', unsafe_allow_html=True)

fraud_types = [
    ("💳", "Credit Card Fraud", "Unauthorized usage of card details for purchases, detected via geolocation patterns."),
    ("🎣", "Phishing Scams", "Deceptive attempts to steal sensitive user credentials, blocked instantly."),
    ("🔓", "Account Takeover", "Malicious actors gaining control of legitimate accounts via credential stuffing."),
    ("🕵️", "Identity Theft", "Stolen personal information used to forge new accounts, flagged by cross-referencing.")
]

cols = st.columns(4)
for i, (icon, title, desc) in enumerate(fraud_types):
    with cols[i]:
        st.markdown(f"""
        <div class="custom-card">
            <div style="font-size: 3rem; margin-bottom: 1rem;">{icon}</div>
            <div style="font-size: 1.25rem; font-weight: 700; margin-bottom: 0.75rem; color: #f8fafc;">{title}</div>
            <div style="font-size: 0.95rem; color: #94a3b8;">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

# 5. Process Section
st.markdown('<h2 style="text-align: center; margin: 4rem 0 2rem; font-weight: 700;">How It Works</h2>', unsafe_allow_html=True)

steps = [
    ("📥", "Data Ingestion", "Securely stream transaction logs via API or batch upload. Supports JSON/CSV."),
    ("🧠", "ML Inference", "Our Random Forest engine analyzes 50+ behavioral features in real-time."),
    ("🛡️", "Instant Verdict", "Receive a 'Legit' or 'Fraud' probability score instantly via webhook.")
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
