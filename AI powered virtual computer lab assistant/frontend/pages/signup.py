import streamlit as st
from backend.database import create_table
create_table()

def app():
    st.markdown("""
        <style>
        .stApp { background: #0a0e1a; }
        .auth-card {
            max-width: 400px;
            margin: 60px auto 0 auto;
            padding: 32px 28px;
            background: #131a2b;
            border: 1px solid #1e293b;
            border-radius: 16px;
        }
        .auth-logo { text-align:center; font-size: 34px; margin-bottom: 4px; }
        .auth-title { text-align:center; color:#f1f5f9; font-size:22px; font-weight:700; margin-bottom:2px; }
        .auth-tagline { text-align:center; color:#64748b; font-size:14px; margin-bottom:22px; }
        div.stButton > button:first-child {
            background: linear-gradient(135deg, #34d399, #059669);
            color: #0a0e1a;
            width: 100%;
            border-radius: 10px;
            height: 3em;
            font-weight: 800;
            border: none;
            font-size: 15px;
            margin-top: 6px;
        }
        div[data-testid="stTextInput"] input {
            background:#0f172a !important;
            color:#e2e8f0 !important;
            border:1px solid #1e293b !important;
            border-radius:8px !important;
        }
        input:-webkit-autofill,
        input:-webkit-autofill:hover,
        input:-webkit-autofill:focus {
            -webkit-box-shadow: 0 0 0px 1000px #0f172a inset !important;
            -webkit-text-fill-color: #e2e8f0 !important;
        }
        .switch-link { text-align:center; color:#64748b; font-size:13px; margin-top:14px; }
        </style>
    """, unsafe_allow_html=True)

    if st.session_state.get("signup_done"):
        st.session_state["signup_done"] = False
        st.session_state["page"] = "Login"
        st.rerun()

    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        st.markdown("""
            <div class="auth-card">
                <div class="auth-logo">🖥️</div>
                <div class="auth-title">Virtual Lab</div>
                <div class="auth-tagline">Create your account to get started</div>
            </div>
        """, unsafe_allow_html=True)

        username = st.text_input(
            "Username", placeholder="Username", key="su_username",
            autocomplete="off", label_visibility="collapsed"
        )
        email = st.text_input(
            "Email", placeholder="Email", key="su_email",
            autocomplete="off", label_visibility="collapsed"
        )
        password = st.text_input(
            "Password", type="password", placeholder="Password (min 8 chars, A-Z, 0-9, symbol)",
            key="su_password", autocomplete="new-password", label_visibility="collapsed"
        )

        if st.button("Create Account"):
            try:
                from backend.auth import signup as backend_signup
                success, msg = backend_signup(username, email, password)
                if success:
                    st.success(f"✅ {msg}")
                    st.info("⏳ Redirecting to Login page...")
                    for key in ["su_username", "su_email", "su_password"]:
                        if key in st.session_state:
                            del st.session_state[key]
                    st.session_state["signup_done"] = True
                    import time
                    time.sleep(1.5)
                    st.rerun()
                else:
                    st.error(f"❌ {msg}")
            except Exception as e:
                st.error(f"Error: {e}")

        st.markdown("<div class='switch-link'>Have an account already?</div>", unsafe_allow_html=True)
        _, mid, _ = st.columns([1.3, 1, 1.3])
        with mid:
            if st.button("Sign In", key="go_login", use_container_width=True):
                st.session_state["page"] = "Login"
                st.rerun()