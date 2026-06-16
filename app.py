import streamlit as st

from frontend.pages import login as login_page

from frontend.pages import signup as signup_page

from frontend.pages import dashboard as dashboard_page

from frontend.pages import learn as learn_page

from frontend.pages import code_editor as code_page

from frontend.pages import teacher_dashboard as teacher_page

from frontend.pages import ai_chat as ai_chat_page



def _apply_css():

    st.markdown("""

        <style>

        .topbar {

          background: linear-gradient(90deg, #001219 0%, #002b36 50%, #023e8a 100%);

          padding: 14px 18px;

          border-radius: 10px;

          color: white;

          margin-bottom: 14px;

        }

        .brand { font-size:20px; font-weight:700 }

        .stButton>button { border-radius:10px; }

        </style>

    """, unsafe_allow_html=True)



def run_app():

    _apply_css()



    # Session States Initialize karein

    if "logged_in" not in st.session_state:

        st.session_state["logged_in"] = False

        st.session_state["username"] = None

   

    # Ye line zaroori hai navigation state ko yaad rakhne ke liye

    if "nav_to" not in st.session_state:

        st.session_state["nav_to"] = "Dashboard"



    if "signup_done" not in st.session_state:

        st.session_state["signup_done"] = False



    st.markdown(

        '<div class="topbar"><span class="brand">🧠 AI Virtual Computer Lab Assistant</span>'

        ' — Learn • Code • Debug • AI Chat</div>',

        unsafe_allow_html=True

    )



    # --- Sidebar Navigation ---

    with st.sidebar:

        st.markdown("## Navigation")

        if st.session_state["logged_in"]:

            pages = ["Dashboard", "Learn", "Code", "AI Chat", "Teacher Dashboard", "Logout"]

           

            # Check karein ke nav_to list mein hai ya nahi

            if st.session_state["nav_to"] not in pages:

                st.session_state["nav_to"] = "Dashboard"

               

            current_idx = pages.index(st.session_state["nav_to"])

           

            # Radio button jo state se connect hai

            choice = st.radio("", pages, index=current_idx, key="main_nav_radio")

           

            # Agar user radio se change kare, toh nav_to update karein

            if choice != st.session_state["nav_to"]:

                st.session_state["nav_to"] = choice

                st.rerun()

        else:

            login_pages = ["Login", "Signup"]

            default_index = 0 if st.session_state.get("signup_done") else 1

            choice = st.radio("", login_pages, index=default_index)



    # --- Routing Logic ---

    if st.session_state["logged_in"]:

        if st.session_state["nav_to"] == "Logout":

            st.session_state["logged_in"] = False

            st.session_state["username"] = None

            st.session_state["nav_to"] = "Dashboard"

            st.rerun()

        elif st.session_state["nav_to"] == "Dashboard":

            dashboard_page.app()

        elif st.session_state["nav_to"] == "Learn":

            learn_page.app()

        elif st.session_state["nav_to"] == "Code":

            code_page.app()

        elif st.session_state["nav_to"] == "AI Chat":

            ai_chat_page.app()

        elif st.session_state["nav_to"] == "Teacher Dashboard":

            teacher_page.app()

    else:

        if choice == "Login":

            ok = login_page.app()

            if ok:

                st.session_state["logged_in"] = True

                st.session_state["nav_to"] = "Dashboard" # Login ke baad seedha dashboard

                st.rerun()

        else:

            signup_page.app()


