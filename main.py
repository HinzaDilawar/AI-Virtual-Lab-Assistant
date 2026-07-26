import streamlit as st

# 1. Page Config (Sabse pehle bina kisi faltu space ke)
st.set_page_config(
    page_title="AI Virtual Lab Assistant",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Theme aur baaki imports
from style_theme import inject_global_css
inject_global_css()

from frontend.app import run_app

# 3. App Runner
if __name__ == "__main__":
    run_app()
