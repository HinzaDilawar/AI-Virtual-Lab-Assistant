import streamlit as st
import random
from backend.database import create_table
create_table()

def _new_puzzle():
    """Do-step calculation — 3+5 jaisa asaan nahi, thoda soch kar hal karna padega"""
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    c = random.randint(3, 20)
    op = random.choice(["+", "-"])
    if op == "+":
        answer = a * b + c
        question = f"({a} × {b}) + {c}"
    else:
        answer = a * b - c
        question = f"({a} × {b}) − {c}"
    return question, answer


def app():
    st.markdown("""
        <style>
        .stApp { background: #0a0e1a; }
        .auth-card {
            max-width: 400px; margin: 50px auto 0 auto; padding: 32px 28px;
            background: #131a2b; border: 1px solid #1e293b; border-radius: 16px;
        }
        .auth-logo { text-align:center; font-size: 34px; margin-bottom: 4px; }
        .auth-title { text-align:center; color:#f1f5f9; font-size:22px; font-weight:700; margin-bottom:2px; }
        .auth-tagline { text-align:center; color:#64748b; font-size:14px; margin-bottom:22px; }
        div.stButton > button:first-child {
            background: linear-gradient(135deg, #38bdf8, #818cf8); color: #0a0e1a;
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
        .puzzle-box {
            background:#1e293b; border-radius:8px; padding:14px; text-align:center;
            font-size:20px; font-weight:700; color:#e2e8f0; margin-bottom:10px;
        }
        </style>
    """, unsafe_allow_html=True)

    from backend.auth import find_account, reset_password

    if "fp_step" not in st.session_state:
        st.session_state["fp_step"] = 1  # 1 = identity check, 2 = puzzle + new password

    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        st.markdown("""
            <div class="auth-card">
                <div class="auth-logo">🔑</div>
                <div class="auth-title">Reset Password</div>
                <div class="auth-tagline">Let's verify it's really you</div>
            </div>
        """, unsafe_allow_html=True)

        # ---------------- STEP 1: Identity check ----------------
        if st.session_state["fp_step"] == 1:
            name = st.text_input("Name", placeholder="Your name", key="fp_name", label_visibility="collapsed")
            email = st.text_input("Email", placeholder="Your registered email", key="fp_email", label_visibility="collapsed")

            if st.button("Continue"):
                ok, msg = find_account(name, email)
                if ok:
                    st.session_state["fp_step"] = 2
                    st.session_state["fp_verified_name"] = name.strip()
                    q, a = _new_puzzle()
                    st.session_state["fp_puzzle_q"] = q
                    st.session_state["fp_puzzle_a"] = a
                    st.rerun()
                else:
                    st.error(f"❌ {msg}")

        # ---------------- STEP 2: Puzzle + new password ----------------
        else:
            if st.session_state.get("fp_error"):
                st.error(f"❌ {st.session_state['fp_error']}")
                st.session_state["fp_error"] = ""

            st.markdown(
                f"<div class='puzzle-box'>🧩 Solve to continue:<br>{st.session_state['fp_puzzle_q']} = ?</div>",
                unsafe_allow_html=True
            )
            puzzle_answer = st.text_input(
                "Puzzle Answer", placeholder="Your answer", key="fp_puzzle_input",
                label_visibility="collapsed"
            )
            new_password = st.text_input(
                "New Password", type="password",
                placeholder="New password (min 8 chars, A-Z, 0-9, symbol)",
                key="fp_new_pass", label_visibility="collapsed"
            )
            confirm_password = st.text_input(
                "Confirm New Password", type="password",
                placeholder="Confirm new password",
                key="fp_confirm_pass", label_visibility="collapsed"
            )

            if st.button("Reset Password"):
                try:
                    solved = puzzle_answer.strip() and int(puzzle_answer.strip()) == st.session_state["fp_puzzle_a"]
                except ValueError:
                    solved = False

                if not solved:
                    q, a = _new_puzzle()
                    st.session_state["fp_puzzle_q"] = q
                    st.session_state["fp_puzzle_a"] = a
                    st.session_state["fp_error"] = "Puzzle answer is incorrect. Here's a new puzzle — try again."
                    st.rerun()
                elif new_password != confirm_password:
                    st.error("❌ Passwords do not match.")
                else:
                    ok, msg = reset_password(st.session_state["fp_verified_name"], new_password)
                    if ok:
                        st.success(f"✅ {msg}")
                        for key in ["fp_step", "fp_name", "fp_email", "fp_verified_name",
                                    "fp_puzzle_q", "fp_puzzle_a", "fp_puzzle_input",
                                    "fp_new_pass", "fp_confirm_pass", "fp_error"]:
                            if key in st.session_state:
                                del st.session_state[key]
                        st.session_state["page"] = "Login"
                        import time
                        time.sleep(1.2)
                        st.rerun()
                    else:
                        st.error(f"❌ {msg}")

        _, mid, _ = st.columns([1.3, 1, 1.3])
        with mid:
            if st.button("Back to Login", key="fp_back", use_container_width=True):
                for key in ["fp_step", "fp_name", "fp_email", "fp_verified_name",
                            "fp_puzzle_q", "fp_puzzle_a", "fp_puzzle_input"]:
                    if key in st.session_state:
                        del st.session_state[key]
                st.session_state["page"] = "Login"
                st.rerun()
