import streamlit as st

 

def inject_global_css():

    st.markdown("""

    <style>

 

    /* ============================================================

       GOOGLE FONTS

    ============================================================ */

    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

 

    /* ============================================================

       ROOT — Soft blue-white background (light content area)

    ============================================================ */

    html, body {

        font-family: 'Inter', sans-serif !important;

    }

 

    [data-testid="stAppViewContainer"] {

        background-color: #EEF2FF !important;

        font-family: 'Inter', sans-serif !important;

    }

 

    [data-testid="stMain"] {

        background: #EEF2FF !important;

    }

 

    /* ============================================================

       SIDEBAR — Deep purple-dark (professional AI feel)

    ============================================================ */

    [data-testid="stSidebar"] {

        background: linear-gradient(180deg, #1E1B4B 0%, #312E81 100%) !important;

        border-right: 1px solid #4338CA !important;

    }

 

    [data-testid="stSidebar"] * {

        color: #E0E7FF !important;

    }

 

    [data-testid="stSidebar"] h1,

    [data-testid="stSidebar"] h2,

    [data-testid="stSidebar"] h3 {

        color: #A5B4FC !important;

        font-weight: 700 !important;

        letter-spacing: 0.05em !important;

        text-transform: uppercase !important;

        font-size: 0.75rem !important;

    }

 

    /* Sidebar nav radio buttons */

    [data-testid="stSidebar"] .stRadio label {

        color: #C7D2FE !important;

        font-weight: 500 !important;

        font-size: 0.95rem !important;

        padding: 6px 0 !important;

    }

 

    [data-testid="stSidebar"] .stRadio label:hover {

        color: #ffffff !important;

    }

 

    /* Sidebar divider */

    [data-testid="stSidebar"] hr {

        border-color: #4338CA !important;

        opacity: 0.5 !important;

    }

 

    /* Sidebar markdown text */

    [data-testid="stSidebar"] p,

    [data-testid="stSidebar"] .stMarkdown p {

        color: #C7D2FE !important;

        font-size: 0.9rem !important;

    }

 

    /* ============================================================

       MAIN CONTENT — Clean readable light panels

    ============================================================ */

 

    /* Page headings */

    [data-testid="stMain"] h1 {

        color: #1E1B4B !important;

        font-weight: 800 !important;

        font-size: 2rem !important;

        letter-spacing: -0.02em !important;

    }

 

    [data-testid="stMain"] h2 {

        color: #312E81 !important;

        font-weight: 700 !important;

    }

 

    [data-testid="stMain"] h3 {

        color: #4338CA !important;

        font-weight: 600 !important;

    }

 

    [data-testid="stMain"] p,

    [data-testid="stMain"] label,

    [data-testid="stMain"] .stMarkdown p {

        color: #1F2937 !important;

        font-size: 0.95rem !important;

    }

 

    /* ============================================================

       CARDS — White panels with soft shadow

    ============================================================ */

    [data-testid="stMetric"] {

        background: #ffffff !important;

        border: 1px solid #E0E7FF !important;

        border-radius: 16px !important;

        padding: 20px !important;

        box-shadow: 0 2px 12px rgba(99, 102, 241, 0.08) !important;

    }

 

    [data-testid="stMetric"] label {

        color: #6366F1 !important;

        font-weight: 600 !important;

        font-size: 0.8rem !important;

        text-transform: uppercase !important;

        letter-spacing: 0.05em !important;

    }

 

    [data-testid="stMetric"] [data-testid="stMetricValue"] {

        color: #1E1B4B !important;

        font-weight: 800 !important;

        font-size: 2rem !important;

    }

 

    /* Forms */

    [data-testid="stForm"] {

        background: #ffffff !important;

        border: 1px solid #E0E7FF !important;

        border-radius: 16px !important;

        padding: 24px !important;

        box-shadow: 0 2px 12px rgba(99, 102, 241, 0.08) !important;

    }

 

    /* Expander */

    .stExpander {

        background: #ffffff !important;

        border: 1px solid #E0E7FF !important;

        border-radius: 12px !important;

    }

 

    /* ============================================================

       CODE EDITOR TEXTAREA — GitHub dark

    ============================================================ */

    .stTextArea textarea {

        background-color: #0D1117 !important;

        color: #93C5FD !important;

        font-family: 'JetBrains Mono', 'Fira Code', 'Source Code Pro', monospace !important;

        font-size: 13px !important;

        line-height: 1.7 !important;

        border: 1px solid #30363D !important;

        border-radius: 10px !important;

    }

 

    /* ============================================================

       INPUT FIELDS — Clean white with indigo focus

    ============================================================ */

    .stTextInput input,

    .stSelectbox select,

    .stNumberInput input {

        background: #ffffff !important;

        border: 1.5px solid #C7D2FE !important;

        border-radius: 10px !important;

        color: #1F2937 !important;

        font-size: 0.95rem !important;

        padding: 10px 14px !important;

        transition: border-color 0.2s ease !important;

    }

 

    .stTextInput input:focus,

    .stNumberInput input:focus {

        border-color: #6366F1 !important;

        box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.15) !important;

        outline: none !important;

    }

 

    /* Selectbox */

    [data-testid="stSelectbox"] > div > div {

        background: #ffffff !important;

        border: 1.5px solid #C7D2FE !important;

        border-radius: 10px !important;

        color: #1F2937 !important;

    }

 

    /* ============================================================

       BUTTONS — Indigo primary, ghost secondary

    ============================================================ */

    .stButton > button {

        background: #6366F1 !important;

        color: #ffffff !important;

        border: none !important;

        border-radius: 10px !important;

        font-weight: 600 !important;

        font-size: 0.9rem !important;

        padding: 10px 20px !important;

        transition: all 0.2s ease !important;

        box-shadow: 0 2px 8px rgba(99, 102, 241, 0.3) !important;

    }

 

    .stButton > button:hover {

        background: #4F46E5 !important;

        box-shadow: 0 4px 16px rgba(99, 102, 241, 0.45) !important;

        transform: translateY(-1px) !important;

    }

 

    .stButton > button:active {

        transform: translateY(0px) !important;

    }

 

    /* Primary (type="primary") — slightly brighter */

    .stButton > button[kind="primary"] {

        background: #6366F1 !important;

    }

 

    /* Download button */

    .stDownloadButton > button {

        background: #ffffff !important;

        color: #6366F1 !important;

        border: 1.5px solid #6366F1 !important;

        border-radius: 10px !important;

        font-weight: 600 !important;

    }

 

    .stDownloadButton > button:hover {

        background: #EEF2FF !important;

    }

 

    /* ============================================================

       ALERTS & STATUS MESSAGES

    ============================================================ */

    /* Success */

    [data-testid="stAlert"][data-baseweb="notification"] {

        border-radius: 12px !important;

        font-weight: 500 !important;

    }

 

    .stSuccess {

        background: #ECFDF5 !important;

        border-left: 4px solid #10B981 !important;

        border-radius: 10px !important;

        color: #065F46 !important;

    }

 

    .stError {

        background: #FEF2F2 !important;

        border-left: 4px solid #EF4444 !important;

        border-radius: 10px !important;

        color: #991B1B !important;

    }

 

    .stWarning {

        background: #FFFBEB !important;

        border-left: 4px solid #F59E0B !important;

        border-radius: 10px !important;

        color: #92400E !important;

    }

 

    .stInfo {

        background: #EFF6FF !important;

        border-left: 4px solid #6366F1 !important;

        border-radius: 10px !important;

        color: #1E40AF !important;

    }

 

    /* ============================================================

       CODE OUTPUT BLOCK — Dark styled

    ============================================================ */

    .stCode, [data-testid="stCode"] {

        background: #0D1117 !important;

        border: 1px solid #30363D !important;

        border-radius: 10px !important;

    }

 

    .stCode code {

        color: #93C5FD !important;

        font-family: 'JetBrains Mono', monospace !important;

        font-size: 13px !important;

    }

 

    /* ============================================================

       DIVIDER

    ============================================================ */

    hr {

        border-color: #E0E7FF !important;

        opacity: 1 !important;

        margin: 16px 0 !important;

    }

 

    /* ============================================================

       SPINNER

    ============================================================ */

    .stSpinner > div {

        border-top-color: #6366F1 !important;

    }

 

    /* ============================================================

       SCROLLBAR — subtle indigo

    ============================================================ */

    ::-webkit-scrollbar { width: 6px; height: 6px; }

    ::-webkit-scrollbar-track { background: #EEF2FF; }

    ::-webkit-scrollbar-thumb {

        background: #A5B4FC;

        border-radius: 10px;

    }

    ::-webkit-scrollbar-thumb:hover { background: #6366F1; }

 

    /* ============================================================

       HIDE STREAMLIT BRANDING

    ============================================================ */

    #MainMenu, footer, header { visibility: hidden !important; }

 

    </style>

    """, unsafe_allow_html=True)