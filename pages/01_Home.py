import streamlit as st
import base64
import os

st.set_page_config(
    page_title="Home - TransactGuard",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- VIDEO BACKGROUND FUNCTION ---
def set_bg_video(video_file):
    if not os.path.exists(video_file):
        st.error(f"Video file not found: {video_file}")
        return

    with open(video_file, "rb") as video:
        video_bytes = video.read()

    encoded = base64.b64encode(video_bytes).decode()

    st.markdown(f"""
    <style>
        .bgvideo {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            z-index: -1;
            overflow: hidden;
            pointer-events: none;
        }}

        .bgvideo > video {{
            width: 100vw;
            height: 100vh;
            object-fit: cover;
            opacity: 0.08;
        }}

        /* FIX STREAMLIT BACKGROUND OVERRIDES */
        html, body, [data-testid="stAppViewContainer"], [data-testid="stMain"] {{
            background-color: transparent !important;
            backdrop-filter: none !important;
        }}
    </style>

    <div class="bgvideo">
        <video autoplay muted loop playsinline id="bgvid">
            <source src="data:video/mp4;base64,{encoded}" type="video/mp4">
        </video>
    </div>

    <script>
        var v = document.getElementById("bgvid");
        if (v) {{
            v.playbackRate = 0.75;
        }}
    </script>
    """, unsafe_allow_html=True)


# --- INJECT VIDEO BEFORE ANY CONTENT ---
set_bg_video("assets/images/0_Global_Market_Financial_Data_3840x2160.mp4")


# --- MAIN CONTENT ---
st.markdown("""
<style>
    [data-testid="stHeader"] {
        display: none;
    }

    .block-container {
        padding-top: 200px;
        padding-bottom: 5rem;
        position: relative;
        z-index: 10;
    }

    .hero-title {
        font-size: 3.5rem;
        font-weight: 800;
        background: linear-gradient(90deg, #3b82f6, #8b5cf6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
    }

    .hero-text {
        color: #94a3b8;
        max-width: 600px;
        margin: 1rem auto 2rem auto;
        text-align: center;
        font-size: 1.1rem;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='hero-title'>Fraud Transaction Prediction</h1>", unsafe_allow_html=True)
st.markdown("<p class='hero-text'>Predict fraudulent transactions with precision and confidence. Our advanced algorithms analyze transaction data in real-time.</p>", unsafe_allow_html=True)


col1, col2, col3 = st.columns([3, 1, 3])
with col2:
    if st.button("🚀 Get Started", use_container_width=True, type="primary"):
        st.switch_page("pages/02_Predict.py")

st.write("---")
st.write("## Real-Life Fraud Transactions")

cols = st.columns(4)
fraud_types = [
    "Unauthorized Credit Card Use",
    "Phishing Scams",
    "Account Takeover",
    "Identity Theft"
]

for i, text in enumerate(fraud_types):
    with cols[i]:
        st.write(f"### {text}")
        st.caption("Description goes here")

st.write("---")
st.write("## Our Process")

cols = st.columns(3)
steps = ["Data Collection", "Analysis and Prediction", "Insights"]

for i, text in enumerate(steps):
    with cols[i]:
        st.write(f"### {text}")
        st.caption("Description goes here")

st.write("---")
st.caption("Built with Streamlit & Machine Learning • © 2025 TransactGuard")
