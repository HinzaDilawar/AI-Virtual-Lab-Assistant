import streamlit as st
from backend.database import create_table
create_table()

def app():
    st.markdown("""
        <style>
        .stApp { background: #0a0e1a; }
        .auth-card {
            max-width: 400px; margin: 60px auto 0 auto; padding: 32px 28px;
            background: #131a2b; border: 1px solid #1e293b; border-radius: 16px;
        }
        .auth-logo { text-align:center; font-size: 34px; margin-bottom: 4px; }
        .auth-title { text-align:center; color:#f1f5f9; font-size:22px; font-weight:700; margin-bottom:2px; }
        .auth-tagline { text-align:center; color:#64748b; font-size:14px; margin-bottom:22px; }
        div.stButton > button:first-child {
            background: linear-gradient(135deg, #38bdf8, #818cf8); color: #0a0e1a;
            width: 100%; border-radius: 10px; height: 3em; font-weight: 800; border: none; font-size: 15px;
            margin-top: 6px;
        }
        .stApp input,
        div[data-testid="stTextInput"] input,
        section.main input {
            background:#ffffff !important; color:#0a0e1a !important;
            border:1px solid #cbd5e1 !important; border-radius:8px !important;
            caret-color:#0a0e1a !important;
            -webkit-text-fill-color: #0a0e1a !important;
        }
        .stApp input::placeholder,
        div[data-testid="stTextInput"] input::placeholder {
            color:#64748b !important;
            -webkit-text-fill-color: #64748b !important;
        }
        input:-webkit-autofill,
        input:-webkit-autofill:hover,
        input:-webkit-autofill:focus,
        input:-webkit-autofill:active {
            -webkit-box-shadow: 0 0 0px 1000px #ffffff inset !important;
            -webkit-text-fill-color: #0a0e1a !important;
            transition: background-color 5000s ease-in-out 0s;
        }
        .switch-link { text-align:center; color:#64748b; font-size:13px; margin-top:14px; }
        </style>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        st.markdown("""
            <div class="auth-card">
                <div class="auth-logo">🖥️</div>
                <div class="auth-title">Virtual Lab</div>
                <div class="auth-tagline">Practice coding with your AI-powered lab</div>
            </div>
        """, unsafe_allow_html=True)

        username_or_email = st.text_input(
            "Username or Email", placeholder="Username or Email", key="li_user",
            autocomplete="one-time-code", label_visibility="collapsed"
        )
        password = st.text_input(
            "Password", type="password", placeholder="Password", key="li_password",
            autocomplete="one-time-code", label_visibility="collapsed"
        )

        if st.button("Sign In"):
            if not username_or_email.strip() or not password.strip():
                st.error("⚠️ Please enter your username/email and password.")
                return False
            try:
                from backend.auth import login as backend_login
                ok, msg = backend_login(username_or_email.strip(), password)
            except Exception as e:
                st.error(f"Backend error: {e}")
                return False
            if ok:
                st.success("✅ Login successful!")
                st.session_state["logged_in"] = True
                st.session_state["username"] = username_or_email.strip()
                st.rerun()
                return True
            else:
                st.error(f"🚫 {msg}")
                return False

        _, midfp, _ = st.columns([1.1, 1.3, 1.1])
        with midfp:
            if st.button("Forgot password?", key="go_forgot", use_container_width=True):
                st.session_state["page"] = "ForgotPassword"
                st.rerun()

        st.markdown("<div class='switch-link'>No account yet?</div>", unsafe_allow_html=True)
        _, mid, _ = st.columns([1.3, 1, 1.3])
        with mid:
            if st.button("Sign Up", key="go_signup", use_container_width=True):
                st.session_state["page"] = "Signup"
                st.rerun()
    return False
