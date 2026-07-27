import streamlit as st
from backend.database import create_table
create_table()

def app():
    st.markdown("""
        <style>
        .stApp { background: #0a0e1a; }
        .auth-card {
            max-width: 420px; margin: 40px auto 0 auto; padding: 32px 28px;
            background: #131a2b; border: 1px solid #1e293b; border-radius: 16px;
        }
        .auth-logo { text-align:center; font-size: 34px; margin-bottom: 4px; }
        .auth-title { text-align:center; color:#f1f5f9; font-size:22px; font-weight:700; margin-bottom:2px; }
        .auth-tagline { text-align:center; color:#64748b; font-size:14px; margin-bottom:22px; }
        div.stButton > button:first-child {
            background: linear-gradient(135deg, #34d399, #059669); color: #0a0e1a;
            width: 100%; border-radius: 10px; height: 3em; font-weight: 800; border: none; font-size: 15px;
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
        .switch-link { text-align:center; color:#64748b; font-size:13px; margin-top:14px; }
        </style>
    """, unsafe_allow_html=True)

    if st.session_state.get("signup_done"):
        st.session_state["signup_done"] = False
        st.session_state["page"] = "Login"
        st.rerun()

    from backend.auth import signup as backend_signup

    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        st.markdown("""
            <div class="auth-card">
                <div class="auth-logo">🖥️</div>
                <div class="auth-title">Virtual Lab</div>
                <div class="auth-tagline">Create your account to get started</div>
            </div>
        """, unsafe_allow_html=True)

        name = st.text_input(
            "Name", placeholder="Name", key="su_name",
            autocomplete="off", label_visibility="collapsed"
        )
        email = st.text_input(
            "Email", placeholder="Email", key="su_email",
            autocomplete="off", label_visibility="collapsed"
        )
        password = st.text_input(
            "Password", type="password",
            placeholder="Min 8 chars, uppercase, number, special char",
            key="su_password", autocomplete="new-password", label_visibility="collapsed"
        )
        confirm_password = st.text_input(
            "Confirm Password", type="password",
            placeholder="Confirm password",
            key="su_confirm_password", autocomplete="new-password", label_visibility="collapsed"
        )
        if password and confirm_password and password != confirm_password:
            st.markdown(
                "<p style='color:#f87171; font-size:12px; margin-top:-8px;'>⚠️ Passwords do not match yet</p>",
                unsafe_allow_html=True
            )
        st.markdown("""
        <div style='background:#1e293b; border-radius:8px; padding:10px 14px; font-size:12px; color:#94a3b8; margin-bottom:14px;'>
        <b>Password must have:</b><br>
        ✅ At least 8 characters<br>
        ✅ One uppercase letter (A-Z)<br>
        ✅ One number (0-9)<br>
        ✅ One special character (!@#$%...)
        </div>
        """, unsafe_allow_html=True)

        if st.button("Create Account"):
            if password != confirm_password:
                st.error("❌ Password and Confirm Password do not match.")
            else:
                success, msg = backend_signup(name, email, password)
                if success:
                    st.success(f"✅ {msg}")
                    for key in ["su_name", "su_email", "su_password", "su_confirm_password"]:
                        if key in st.session_state:
                            del st.session_state[key]
                    st.session_state["signup_done"] = True
                    import time
                    time.sleep(1.2)
                    st.rerun()
                else:
                    st.error(f"❌ {msg}")

        st.markdown("<div class='switch-link'>Have an account already?</div>", unsafe_allow_html=True)
        _, mid, _ = st.columns([1.3, 1, 1.3])
        with mid:
            if st.button("Sign In", key="go_login", use_container_width=True):
                st.session_state["page"] = "Login"
                st.rerun()
