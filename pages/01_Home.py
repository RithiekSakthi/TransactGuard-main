import streamlit as st
import base64

st.set_page_config(
    page_title="Home - TransactGuard",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ------------ READ AND ENCODE VIDEO -----------------
def get_video_html(path):
    with open(path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    return f"""
<div class="video-bg">
  <video autoplay muted loop playsinline>
    <source src="data:video/mp4;base64,{encoded}" type="video/mp4">
  </video>
</div>

<style>
.video-bg {{
    position: fixed;
    top: 180px;  /* BELOW BANNER */
    left: 0;
    width: 100vw;
    height: calc(100vh - 180px);
    overflow: hidden;
    z-index: -1;
}}

.video-bg video {{
    position: absolute;
    top: 50%;
    left: 50%;
    min-width: 100%;
    min-height: 100%;
    transform: translate(-50%, -50%);
    object-fit: cover;
    opacity: 0.05;
}}

/* Make background completely transparent */
[data-testid="stAppViewContainer"],
[data-testid="stMain"],
body {{
    background: transparent !important;
}}
</style>

<script>
  const vid = document.querySelector(".video-bg video");
  if (vid) {{
      vid.playbackRate = 0.8;
  }}
</script>
"""

# -------------------------------------------------------

# ------------ CUSTOM CSS (MODIFIED) --------------------
st.markdown("""
<style>

    /* REMOVE SIDEBAR */
    [data-testid="stSidebar"], [data-testid="collapsedControl"] {
        display: none;
    }

    /* REMOVE DEFAULT HEADER */
    [data-testid="stHeader"] {
        display: none;
    }

    .block-container {
        padding-top: 220px; 
        padding-bottom: 5rem;
    }

    /* Original colors */
    :root {
        --primary-color: #3b82f6;
        --background-dark: #0f172a;
        --card-bg: rgba(30, 41, 59, 0.7);
        --text-primary: #f8fafc;
        --text-secondary: #94a3b8;
        --accent-gradient: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%);
    }

    /* KEEP MENU STYLE EXACTLY SAME */
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
        cursor: pointer;
        transition: .3s;
    }

    .fab-icon {
        font-size: 28px;
        color: white;
    }

    .fab-list {
        position: absolute;
        top: 0;
        left: 0;
        width: 65px;
        height: 65px;
        pointer-events: none;
    }

    .fab-item {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%,-50%);
        width: 50px;
        height: 50px;
        border-radius: 50%;
        background: rgba(30,41,59,.9);
        border: 1px solid rgba(255,255,255,.1);
        backdrop-filter: blur(8px);
        display: flex;
        justify-content:center;
        align-items:center;
        opacity: 0;
        transition: .35s;
        cursor:pointer;
    }

    .fab-label {
        position: absolute;
        left: 60px;
        background: #1e293b;
        color: #fff;
        padding: 5px 12px;
        border-radius: 6px;
        font-size: 13px;
        opacity: 0;
        visibility: hidden;
        tr
