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
        }
        div[data-testid="stTextInput"] input {
            background:#0f172a !important; color:#e2e8f0 !important;
            border:1px solid #1e293b !important; border-radius:8px !important;
        }
        </style>
    """, unsafe_allow_html=True)

    from backend.auth import request_password_reset, reset_password

    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        st.markdown("""
            <div class="auth-card">
                <div class="auth-logo">🔑</div>
                <div class="auth-title">Reset Password</div>
                <div class="auth-tagline">We'll email you a 6-digit code</div>
            </div>
        """, unsafe_allow_html=True)

        if "reset_email_sent" not in st.session_state:
            st.session_state["reset_email_sent"] = False

        if not st.session_state["reset_email_sent"]:
            email = st.text_input("Email", placeholder="Your registered email", key="fp_email", label_visibility="collapsed")
            if st.button("Send Reset Code"):
                if not email.strip():
                    st.error("⚠️ Please enter your email.")
                else:
                    ok, msg = request_password_reset(email)
                    if ok:
                        st.session_state["reset_email_sent"] = True
                        st.session_state["reset_email"] = email.strip().lower()
                        st.success(f"✅ {msg}")
                        st.rerun()
                    else:
                        st.error(f"❌ {msg}")
        else:
            st.info(f"Code sent to {st.session_state['reset_email']}")
            code = st.text_input("Code", placeholder="6-digit code", key="fp_code", label_visibility="collapsed")
            new_password = st.text_input(
                "New Password", type="password",
                placeholder="New password (min 8 chars, A-Z, 0-9, symbol)",
                key="fp_new_pass", label_visibility="collapsed"
            )
            if st.button("Reset Password"):
                ok, msg = reset_password(st.session_state["reset_email"], code, new_password)
                if ok:
                    st.success(f"✅ {msg}")
                    st.session_state["reset_email_sent"] = False
                    st.session_state["page"] = "Login"
                    import time
                    time.sleep(1.2)
                    st.rerun()
                else:
                    st.error(f"❌ {msg}")

        _, mid, _ = st.columns([1.3, 1, 1.3])
        with mid:
            if st.button("Back to Login", key="fp_back", use_container_width=True):
                st.session_state["reset_email_sent"] = False
                st.session_state["page"] = "Login"
                st.rerun()