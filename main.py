import streamlit as st

st.set_page_config(
    page_title="AI Virtual Lab Assistant",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

from style_theme import inject_global_css
inject_global_css()

from frontend.app import run_app

if __name__ == "__main__":
    run_app()
