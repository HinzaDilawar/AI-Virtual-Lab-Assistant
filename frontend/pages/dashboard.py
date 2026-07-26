import streamlit as st

def _card(emoji, title, desc, color="#0077b6"):
    st.markdown(f"""
    <div style="border:1px solid {color}; border-radius:12px; padding:14px;
                background:#f0f8ff; margin-bottom:8px; min-height:100px;">
      <div style="font-size:28px;">{emoji}</div>
      <div style="font-weight:700; font-size:15px; margin-top:4px;">{title}</div>
      <div style="color:{color}; font-size:12px; margin-top:4px;">{desc}</div>
    </div>
    """, unsafe_allow_html=True)

def app():
    if not st.session_state.get("logged_in"):
        st.warning("⚠️ Please login first")
        return

    st.title("📊 Dashboard")
    st.write(f"Welcome, **{st.session_state.get('username', 'Student')}** 👋")

    # ── Modules Overview ──
    st.subheader("Modules Overview")
    c1, c2, c3 = st.columns(3)

    with c1:
        _card("📘", "📚 Learn", "Browse 150 programs — Python, C++, JavaScript")
        if st.button("Open Learn →", key="mod_learn", use_container_width=True):
            st.session_state["nav_to"] = "Learn"
            # Agar direct main Learn tab se jayein, toh default "Python" set rahe
            st.session_state["learn_lang"] = "Python"
            st.rerun()

    with c2:
        _card("🖥️", "💻 Code Editor", "Write, run & debug multi-language code")
        if st.button("Open Code →", key="mod_code", use_container_width=True):
            st.session_state["nav_to"] = "Code"
            st.rerun()

    with c3:
        _card("🤖", "🤖 AI Assistant", "Ask any question — coding, concepts, debugging")
        if st.button("Open AI Chat →", key="mod_ai", use_container_width=True):
            st.session_state["nav_to"] = "AI Chat"
            st.rerun()

    st.markdown("---")

    # ── Quick Access ──
    st.subheader("Quick Access")
    c4, c5, c6, c7 = st.columns(4)

    with c4:
        _card("🐍", "Python Learn", "View Python programs", "#2d6a4f")
        if st.button("Open Python →", key="qa_python", use_container_width=True):
            st.session_state["nav_to"] = "Learn"
            st.session_state["learn_lang"] = "Python"  # Forced Python State
            st.rerun()

    with c5:
        _card("💠", "C++ Learn", "View C++ programs", "#1d3557")
        if st.button("Open C++ →", key="qa_cpp", use_container_width=True):
            st.session_state["nav_to"] = "Learn"
            st.session_state["learn_lang"] = "C++"     # Forced C++ State
            st.rerun()

    with c6:
        _card("📜", "JavaScript Learn", "View JavaScript programs", "#b5451b")
        if st.button("Open JS →", key="qa_js", use_container_width=True):
            st.session_state["nav_to"] = "Learn"
            st.session_state["learn_lang"] = "JavaScript"  # Forced JavaScript State
            st.rerun()

    with c7:
        _card("🧑‍🏫", "Teacher Dashboard", "View all student progress & activity", "#6b21a8")
        if st.button("Open Teacher →", key="qa_teacher", use_container_width=True):
            st.session_state["nav_to"] = "Teacher Dashboard"
            st.rerun()


