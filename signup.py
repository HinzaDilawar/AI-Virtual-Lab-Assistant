import streamlit as st
from backend.database import create_table

create_table()

def app():
    st.markdown("""
        <style>
        div.stButton > button:first-child {
            background: linear-gradient(135deg, #34d399, #059669);
            color: #0a0e1a;
            width: 100%;
            border-radius: 10px;
            height: 3em;
            font-weight: 800;
            border: none;
            font-size: 15px;
        }
        /* Hide browser autofill saved info */
        input:-webkit-autofill,
        input:-webkit-autofill:hover,
        input:-webkit-autofill:focus {
            -webkit-box-shadow: 0 0 0px 1000px #1e293b inset !important;
            -webkit-text-fill-color: #e2e8f0 !important;
        }
        </style>
    """, unsafe_allow_html=True)

    # Agar already signup ho gaya to login page pe bhejo
    if st.session_state.get("signup_done"):
        st.session_state["signup_done"] = False
        st.session_state["page"] = "Login"
        st.rerun()

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<h2 style='text-align:center;'>📝 Create Account</h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center; color:#64748b;'>Fill in all fields to register.</p>", unsafe_allow_html=True)
        st.divider()

        # autocomplete="off" se browser saved info show nahi karega
        st.markdown("""
            <script>
            window.addEventListener('load', function() {
                document.querySelectorAll('input').forEach(function(el) {
                    el.setAttribute('autocomplete', 'new-password');
                });
            });
            </script>
        """, unsafe_allow_html=True)

        username = st.text_input(
            "👤 Username",
            placeholder="e.g. ali_dev",
            key="su_username",
            autocomplete="off"
        )
        email = st.text_input(
            "📧 Email Address",
            placeholder="e.g. ali@gmail.com",
            key="su_email",
            autocomplete="off"
        )
        password = st.text_input(
            "🔒 Password",
            type="password",
            placeholder="Min 8 chars, uppercase, number, special char",
            key="su_password",
            autocomplete="new-password"
        )

        st.markdown("""
        <div style='background:#1e293b; border-radius:8px; padding:10px 14px; font-size:12px; color:#94a3b8; margin-bottom:10px;'>
        <b>Password must have:</b><br>
        ✅ At least 8 characters<br>
        ✅ One uppercase letter (A-Z)<br>
        ✅ One number (0-9)<br>
        ✅ One special character (!@#$%...)
        </div>
        """, unsafe_allow_html=True)

        if st.button("Create Account"):
            try:
                from backend.auth import signup as backend_signup
                success, msg = backend_signup(username, email, password)
                if success:
                    st.success(f"✅ {msg}")
                    st.info("⏳ Redirecting to Login page...")
                    # Session clear karo takey fields empty hon
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