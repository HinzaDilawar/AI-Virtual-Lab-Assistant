import streamlit as st
from backend.ai_assistant import chat_with_ai

def app():
    if not st.session_state.get("logged_in"):
        st.warning("⚠️ Please login first")
        return

    st.title("🤖 AI Assistant")
    st.write("Ask me anything — coding, concepts, debugging, or general questions!")

    st.markdown("""
        <style>
        .chat-user {
            background: #e0f2fe;
            border-radius: 12px 12px 2px 12px;
            padding: 10px 14px;
            margin: 6px 0;
            color: #0c4a6e;
            font-size: 14px;
            text-align: right;
        }
        .chat-ai {
            background: #f1f5f9;
            border-radius: 12px 12px 12px 2px;
            padding: 10px 14px;
            margin: 6px 0;
            color: #1e293b;
            font-size: 14px;
            border-left: 3px solid #38bdf8;
        }
        .chat-label-user { font-size:11px; color:#64748b; text-align:right; margin-bottom:2px; }
        .chat-label-ai   { font-size:11px; color:#38bdf8; margin-bottom:2px; font-weight:700; }
        [data-testid="stForm"] { border: none; padding: 0; }
        
        /* 🚫 Global Hack: Chat input box ke autofill popup dropdown ko hide karne ke liye */
        input:-webkit-autofill,
        input:-webkit-autofill:hover,
        input:-webkit-autofill:focus,
        input:-webkit-autofill:active {
            -webkit-box-shadow: 0 0 0px 1000px #1e293b inset !important;
            -webkit-text-fill-color: #e2e8f0 !important;
            transition: background-color 5000s ease-in-out 0s;
        }
        input {
            autocomplete: off !important;
        }
        </style>
    """, unsafe_allow_html=True)

    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []

    # Chat display container
    chat_container = st.container()
    with chat_container:
        for msg in st.session_state["chat_history"]:
            if msg["role"] == "user":
                st.markdown(f'<div class="chat-label-user">You</div><div class="chat-user">{msg["content"]}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="chat-label-ai">🤖 AI Assistant</div><div class="chat-ai">{msg["content"]}</div>', unsafe_allow_html=True)

    # Input handling without full page rerun trigger
    with st.form(key="ai_chat_form", clear_on_submit=True):
        col_inp, col_btn = st.columns([5, 1])
        with col_inp:
            # 👤 Strict Autofill Blocked Chat Input Box
            user_input = st.text_input(
                "", 
                placeholder="Type your question here...", 
                label_visibility="collapsed",
                key="chat_user_input_field",
                autocomplete="one-time-code"  # <-- Browser suggestion history mitaane ka hack
            )
        with col_btn:
            submit = st.form_submit_button("Send 📤", use_container_width=True, type="primary")

        if submit and user_input.strip():
            # Message history update
            st.session_state["chat_history"].append({"role": "user", "content": user_input.strip()})
            
            try:
                # Backend se response lena
                reply = chat_with_ai(user_input.strip())
            except Exception as e:
                reply = f"❌ Error: {str(e)}"
            
            st.session_state["chat_history"].append({"role": "ai", "content": reply})
            st.rerun()

    # Clear chat logic
    if len(st.session_state["chat_history"]) > 0:
        if st.button("🗑️ Clear Chat", key="clear_chat_btn"):
            st.session_state["chat_history"] = []
            st.rerun()