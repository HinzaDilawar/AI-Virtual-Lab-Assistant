import re

import streamlit as st

import tempfile

import subprocess

import os

import sys

import hashlib

import time

from pathlib import Path



# ── Backend Modules Import ──────────────────────────────────────────────────

from backend.run import execute_any_language



try:

    from backend.progress import add_progress

    from backend.code_checker import check_code

except ImportError:

    pass



# ── Language config (Updated with Node.js support hints) ───────────────────

LANGUAGES = {

    "Python 🐍": {

        "extension": ".py",  

        "label": "python",

        "default_code": "# write python code"

    },

    "C++ ⚙️": {

        "extension": ".cpp",

        "label": "cpp",

        "default_code": "// write c++ code"

    },

    "JavaScript 🌐": {

        "extension": ".js",  

        "label": "javascript",

        # Default code ko thoda meaningful kar diya taake test karne me asaani ho

        "default_code": "// write javascript code"

    },

}



# ── Dynamic Input Prompt Extractor ───────────────────────────────────────────

def _extract_input_prompts(code: str, label: str) -> list:

    prompts = []

    clean = re.sub(r'/\*.*?\*/', '', code, flags=re.DOTALL)

 

    if label == "python":

        lines = [l for l in clean.splitlines() if not l.strip().startswith('#')]

        src = "\n".join(lines)

        for m in re.finditer(r'\binput\s*\(\s*(["\'])(.*?)\1\s*\)', src):

            raw = m.group(2).strip()

            raw = raw.replace('\\n', '').replace('\\t', '').rstrip(':').rstrip('?').strip()

            prompts.append(raw if raw else "Enter value")

        for _ in re.finditer(r'\binput\s*\(\s*\)', src):

            prompts.append("Enter value")

 

    elif label == "cpp":

        lines = [l for l in clean.splitlines() if not l.strip().startswith('//')]

        src = "\n".join(lines)

        cout_strings = re.findall(r'cout\s*<<\s*"([^"]+)"', src)

        cin_count    = len(re.findall(r'\bcin\s*>>', src))

        getline_count = len(re.findall(r'\bgetline\s*\(', src))

        total = cin_count + getline_count

        filtered = []

        for s in cout_strings:

            s = s.replace('\\n', '').replace('\\t', '').strip().rstrip(':').rstrip('?').strip()

            if len(s) > 1:

                filtered.append(s)

        while len(filtered) < total:

            filtered.append(f"Enter value {len(filtered)+1}")

        prompts = filtered[:total]

 

    elif label == "javascript":

        lines = [l for l in clean.splitlines() if not l.strip().startswith('//')]

        src = "\n".join(lines)

        for m in re.finditer(r'rl\.question\s*\(\s*["`\'](.*?)["`\']', src, re.DOTALL):

            raw = re.sub(r'\\n', ' ', m.group(1)).strip().rstrip(':').rstrip('?').strip()

            prompts.append(raw if raw else "Enter value")

 

    return prompts



def _needs_input(code: str, label: str) -> bool:

    clean = re.sub(r'#.*',        '', code)

    clean = re.sub(r'//.*',       '', clean)

    clean = re.sub(r'/\*.*?\*/',  '', clean, flags=re.DOTALL)

    patterns = {

        "python":      [r'\binput\s*\('],

        "cpp":         [r'\bcin\s*>>', r'\bgetline\s*\(', r'\bscanf\s*\('],

        "javascript": [r'\brl\.question\s*\(', r'\bprocess\.stdin', r'\breadline\b'],

    }

    return any(re.search(p, clean) for p in patterns.get(label, []))



# ── Save + display result ─────────────────────────────────────────────────────

def _save_and_show(success, output, elapsed, code, selected_lang, label, col_res):

    if label == "python":

        try:

            is_valid, msg, hint, solution = check_code(code)

            ai_feedback = f"✅ {msg}" if is_valid else f"❌ {msg}\n💡 {hint}\n🔧 {solution}"

        except Exception:

            ai_feedback = "✅ Code ran successfully!" if success else f"❌ Error:\n{output}"

    else:

        ai_feedback = "✅ Code ran successfully!" if success else f"❌ Error:\n{output}"



    if "submissions" not in st.session_state:

        st.session_state["submissions"] = []



    st.session_state["submissions"].append({

        "language": selected_lang, "code": code,

        "status": "Success" if success else "Error",

        "output": output, "ai_feedback": ai_feedback, "elapsed": elapsed,

    })

   

    if st.session_state.get("username"):

        try:

            add_progress(st.session_state["username"], label,

                         "Completed" if success else "Attempted")

        except NameError:

            pass



    with col_res:

        if success:

            st.success("✅ Code ran successfully!")

            st.code(output, language="text")

        else:

            st.error("❌ Error found!")

            st.code(output, language="text")



# ── Main App ──────────────────────────────────────────────────────────────────

def app():

    st.markdown("""

        <style>

        .stTextArea textarea {

            font-family: 'JetBrains Mono', 'Fira Code', monospace;

            background-color: #0d1117;

            color: #93c5fd;

            border-radius: 10px;

            font-size: 13px;

            line-height: 1.6;

        }

        .stButton>button { border-radius: 8px; }

        </style>

    """, unsafe_allow_html=True)



    if "submissions" not in st.session_state: st.session_state["submissions"] = []

    if "current_lang" not in st.session_state: st.session_state["current_lang"] = "Python 🐍"

    if "awaiting_input" not in st.session_state: st.session_state["awaiting_input"] = False

    if "pending_code" not in st.session_state: st.session_state["pending_code"] = ""



    # ── Header ────────────────────────────────────────────────────────────────

    col_t1, col_t2 = st.columns([3, 1])

    with col_t1:

        st.title("💻 Virtual Lab Code Editor")

    with col_t2:

        selected_lang = st.selectbox(

            "🗣️ Language",

            options=list(LANGUAGES.keys()),

            index=list(LANGUAGES.keys()).index(st.session_state["current_lang"]),

        )

        if selected_lang != st.session_state["current_lang"]:

            st.session_state["current_lang"] = selected_lang

            st.session_state["awaiting_input"] = False

            st.session_state["pending_code"] = ""

            st.rerun()



    st.divider()



    lang_cfg = LANGUAGES[selected_lang]

    label    = lang_cfg["label"]



    col_code, col_res = st.columns([1.8, 1])



    # ── Editor ────────────────────────────────────────────────────────────────

    with col_code:

        st.subheader("📝 Editor")



        editor_key = f"editor_{label}"

        if editor_key not in st.session_state:

            st.session_state[editor_key] = lang_cfg["default_code"]



        code = st.text_area(

            "code_area",

            value=st.session_state[editor_key],

            height=420,

            label_visibility="collapsed",

            key=f"textarea_{label}",

        )

        st.session_state[editor_key] = code



        c1, c2, c3 = st.columns(3)

        with c1:

            run_btn  = st.button("🚀 Run Code", type="primary", use_container_width=True)

        with c2:

            hint_btn = st.button("💡 AI Hint", use_container_width=True)

        with c3:

            st.download_button("💾 Download", data=code,

                               file_name=f"main{lang_cfg['extension']}",

                               use_container_width=True)



    # ── Output panel ──────────────────────────────────────────────────────────

    with col_res:

        st.subheader("🖥️ Output")



        is_default = code.strip() == lang_cfg["default_code"].strip()



        # ── SYSTEM PATH FIX ──

        # Node.js ka executable path force karne ke liye hum runtime par PATH inject kar rahe hain

        node_path = r"C:\Program Files\nodejs"

        if node_path not in os.environ["PATH"]:

            os.environ["PATH"] += os.pathsep + node_path



        if run_btn:

            if not code.strip() or is_default:

                st.warning("Please write some code first.")

                st.session_state["awaiting_input"] = False

            elif _needs_input(code, label):

                st.session_state["awaiting_input"] = True

                st.session_state["pending_code"]   = code

            else:

                st.session_state["awaiting_input"] = False

                with st.spinner("Running…"):

                    # Yeh call aapke backend/run.py ko chalati hai

                    success, output, elapsed = execute_any_language(label, code, [])

                _save_and_show(success, output, elapsed, code, selected_lang, label, col_res)



        # ── Multi-field dynamic inputs render ──

        if st.session_state["awaiting_input"] and st.session_state["pending_code"]:

            saved_code = st.session_state["pending_code"]

            prompts    = _extract_input_prompts(saved_code, label)



            if not prompts:

                prompts = ["Enter value"]



            st.markdown("**📥 Program Input**")

           

            values = []

            for i, prompt in enumerate(prompts):

                val = st.text_input(

                    label=f"{prompt}:",

                    key=f"inp_{i}_{label}_{len(saved_code)}",

                    placeholder=f"Type here…"

                )

                values.append(val)



            run_input_btn = st.button("▶️ Enter & Run", type="primary", use_container_width=True)



            if run_input_btn:

                if any(v.strip() == "" for v in values):

                    st.warning("⚠️ Sab fields mein value daalo phir dobara Run karein.")

                else:

                    with st.spinner("Running…"):

                        success, output, elapsed = execute_any_language(label, saved_code, values)

                   

                    if output == "INPUT_NEEDED":

                        st.error("❌ Inputs missing or mismatched!")

                    else:

                        st.session_state["awaiting_input"] = False

                        st.session_state["pending_code"]   = ""

                        _save_and_show(success, output, elapsed, saved_code, selected_lang, label, col_res)



        # AI Hint

        if hint_btn:

            if not code.strip():

                st.info("Write some code first.")

            else:

                with st.spinner("Getting AI hint…"):

                    try:

                        from backend.ai_assistant import get_hint

                        hint_text = get_hint(label, code)

                    except Exception:

                        hint_text = "Tip: Check your syntax, variable names, and logic flow."

                st.info(f"💡 {hint_text}")



    # ── Sidebar ───────────────────────────────────────────────────────────────

    with st.sidebar:

        st.header("🤖 AI Feedback")

        if st.session_state.get("submissions"):

            latest = st.session_state["submissions"][-1]

            st.markdown(f"**Language:** {latest['language']}")

            st.markdown(f"**Status:** {latest['status']}")

            st.markdown(f"**Time:** {latest['elapsed']:.2f}s")

            st.divider()

            st.markdown(latest["ai_feedback"])

        else:

            st.info("Run your code to see AI feedback here.")

