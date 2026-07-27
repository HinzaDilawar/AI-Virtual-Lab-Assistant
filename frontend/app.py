import streamlit as st

from frontend.pages import login as login_page
from frontend.pages import signup as signup_page
from frontend.pages import forgot_password as forgot_password_page
from frontend.pages import dashboard as dashboard_page
from frontend.pages import learn as learn_page
from frontend.pages import code_editor as code_page
from frontend.pages import teacher_dashboard as teacher_page
from frontend.pages import ai_chat as ai_chat_page


def _apply_css():
    st.markdown("""
        <style>
        .topbar {
          background: linear-gradient(90deg, #001219 0%, #002b36 50%, #023e8a 100%);
          padding: 14px 18px;
          border-radius: 10px;
          color: white;
          margin-bottom: 14px;
        }
        .brand { font-size:20px; font-weight:700 }
        .stButton>button { border-radius:10px; }
        </style>
    """, unsafe_allow_html=True)


def run_app():
    _apply_css()

    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False
        st.session_state["username"] = None

    if "nav_to" not in st.session_state:
        st.session_state["nav_to"] = "Dashboard"

    if "signup_done" not in st.session_state:
        st.session_state["signup_done"] = False

    if "page" not in st.session_state:
        st.session_state["page"] = "Signup" if st.session_state.get("signup_done") else "Login"

    st.markdown(
        '<div class="topbar"><span class="brand">🧠 AI Virtual Computer Lab Assistant</span>'
        ' — Learn • Code • Debug • AI Chat</div>',
        unsafe_allow_html=True
    )

    with st.sidebar:
        st.markdown("## Navigation")
        if st.session_state["logged_in"]:
            pages = ["Dashboard", "Learn", "Code", "AI Chat", "Teacher Dashboard", "Logout"]

            if st.session_state["nav_to"] not in pages:
                st.session_state["nav_to"] = "Dashboard"

            current_idx = pages.index(st.session_state["nav_to"])
            choice = st.radio("", pages, index=current_idx, key="main_nav_radio")

            if choice != st.session_state["nav_to"]:
                st.session_state["nav_to"] = choice
                st.rerun()
        else:
            login_pages = ["Login", "Signup"]
            radio_default = st.session_state["page"] if st.session_state["page"] in login_pages else "Login"
            default_index = login_pages.index(radio_default)

            choice = st.radio("", login_pages, index=default_index, key="auth_nav_radio")

            # 🔑 Sirf tab sync karo jab hum already Login/Signup pe hon —
            # warna ye ForgotPassword state ko hamesha wapas "Login" pe overwrite kar deta tha.
            if st.session_state["page"] in login_pages and choice != st.session_state["page"]:
                st.session_state["page"] = choice
                st.rerun()

    if st.session_state["logged_in"]:
        if st.session_state["nav_to"] == "Logout":
            st.session_state["logged_in"] = False
            st.session_state["username"] = None
            st.session_state["nav_to"] = "Dashboard"
            st.session_state["page"] = "Login"
            st.rerun()
        elif st.session_state["nav_to"] == "Dashboard":
            dashboard_page.app()
        elif st.session_state["nav_to"] == "Learn":
            learn_page.app()
        elif st.session_state["nav_to"] == "Code":
            code_page.app()
        elif st.session_state["nav_to"] == "AI Chat":
            ai_chat_page.app()
        elif st.session_state["nav_to"] == "Teacher Dashboard":
            teacher_page.app()
    else:
        if st.session_state["page"] == "Login":
            ok = login_page.app()
            if ok:
                st.session_state["logged_in"] = True
                st.session_state["nav_to"] = "Dashboard"
                st.rerun()
        elif st.session_state["page"] == "Signup":
            signup_page.app()
        elif st.session_state["page"] == "ForgotPassword":
            forgot_password_page.app()
        else:
            st.session_state["page"] = "Login"
            st.rerun()




