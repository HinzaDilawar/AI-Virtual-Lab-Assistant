import streamlit as st
from backend.database import create_table

create_table()

def app():
    st.markdown("""
        <style>
        div.stButton > button:first-child {
            background: linear-gradient(135deg, #38bdf8, #818cf8);
            color: #0a0e1a;
            width: 100%;
            border-radius: 10px;
            height: 3em;
            font-weight: 800;
            border: none;
            font-size: 15px;
        }
        
        /* 🚫 Global Hack: Chrome Autofill Dropdown Background aur Text Box control */
        input:-webkit-autofill,
        input:-webkit-autofill:hover,
        input:-webkit-autofill:focus,
        input:-webkit-autofill:active {
            -webkit-box-shadow: 0 0 0px 1000px #1e293b inset !important;
            -webkit-text-fill-color: #e2e8f0 !important;
            transition: background-color 5000s ease-in-out 0s;
        }
        
        /* Browser ke built-in autocomplete indicators ko override karne ke liye */
        input {
            autocomplete: off !important;
        }
        </style>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        st.markdown("<h2 style='text-align:center;'>🔐 Student Login</h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center; color:#64748b;'>Login with your username or email.</p>", unsafe_allow_html=True)
        st.divider()

        # 👤 Strict Autofill Blocked Input
        username_or_email = st.text_input(
            "👤 Username or Email",
            placeholder="Enter username or email",
            key="li_user",
            autocomplete="one-time-code"  # <-- Chrome dropdown ko block karne ka hack
        )
        
        # 🔒 Strict Saved Password Popup Blocked Input
        password = st.text_input(
            "🔒 Password",
            type="password",
            placeholder="Enter your password",
            key="li_password",
            autocomplete="one-time-code"  # <-- Chrome saved info dialog box block karne ka hack
        )

        st.write("")
        if st.button("Login to Lab"):
            if not username_or_email.strip() or not password.strip():
                st.error("⚠️ Please enter your username/email and password.")
                return False

            try:
                from backend.auth import login as backend_login
                ok = backend_login(username_or_email.strip(), password)
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
                st.error("🚫 Invalid credentials. Check your username/email or password.")
                return False

    return False

