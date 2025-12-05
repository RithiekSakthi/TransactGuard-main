import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Data - TransactGuard",
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

    /* --- DATA SPECIFIC STYLES --- */
    .card {
        background-color: var(--card-bg);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 1.5rem;
        backdrop-filter: blur(10px);
        height: 100%;
    }
    h1, h2, h3, h4, p { font-family: 'Inter', sans-serif !important; }
    
    /* Plotly and Input corrections */
    .stSelectbox > div > div > div { background-color: rgba(15, 23, 42, 0.8) !important; color: white !important; }
    .stCheckbox label { color: white !important; }
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

@st.cache_data
def load_sample_data():
    np.random.seed(42)
    df = pd.DataFrame({
        "AMOUNT_TO_SENDER_BALANCE": np.random.uniform(0, 2, 1000),
        "RECEIVER_INIT_BALANCE": np.random.exponential(2000, 1000),
        "SENDER_INIT_BALANCE": np.random.exponential(3000, 1000),
        "HOUR": np.random.randint(0, 24, 1000),
        "DAY": np.random.choice(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], 1000),
        "IS_FRAUD": np.random.choice([0, 1], 1000, p=[0.9, 0.1])
    })
    return df

df = load_sample_data()

st.markdown('<h1 style="font-size: 32px; font-weight: 700; margin-bottom: 2rem; color: #f8fafc; text-align: center;">Interactive Data Explorer</h1>', unsafe_allow_html=True)

col_left, col_center, col_right = st.columns([1, 2.5, 1.2], gap="large")

with col_left:
    st.markdown("""
    <div class="card">
        <h4 style="color: var(--primary-color);">Key Statistics</h4>
        <div style="font-size: 14px; line-height: 2.2; color: var(--text-secondary);">
            <strong style="color: white;">Total Transactions:</strong> 1,342,155<br>
            <strong style="color: white;">Date Range:</strong> Jan '23 - Dec '23<br>
            <strong style="color: white;">Avg Amount:</strong> $1,204.58<br>
            <strong style="color: white;">Median Amount:</strong> $899.12
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_center:
    fraud_mask = df["IS_FRAUD"] == 1
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df[~fraud_mask]["AMOUNT_TO_SENDER_BALANCE"], y=df[~fraud_mask]["RECEIVER_INIT_BALANCE"], mode='markers', marker=dict(size=6, color='#0066ff', opacity=0.6), name='Legitimate'))
    fig.add_trace(go.Scatter(x=df[fraud_mask]["AMOUNT_TO_SENDER_BALANCE"], y=df[fraud_mask]["RECEIVER_INIT_BALANCE"], mode='markers', marker=dict(size=8, color='#ff6b9d'), name='Fraudulent'))
    
    fig.update_layout(
        title="Amount Ratio vs. Receiver Balance", 
        template="plotly_dark", 
        height=400,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=20, r=20, t=40, b=20)
    )
    st.plotly_chart(fig, use_container_width=True)

with col_right:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<h4 style="color: var(--primary-color);">Controls</h4>', unsafe_allow_html=True)
    
    x_axis = st.selectbox("X-Axis", df.columns)
    y_axis = st.selectbox("Y-Axis", df.columns, index=1)
    show_trend = st.checkbox("Show Trendline", value=True)
    if st.button("🔄 Update Plot", use_container_width=True, type="primary"):
        st.info("Plot updated!")
    st.markdown('</div>', unsafe_allow_html=True)
