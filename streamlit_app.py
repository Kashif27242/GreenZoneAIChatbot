import streamlit as st
from components.header import show_header
from components.footer import show_footer
from pages import home, about, contact, auth
import mybot  # <-- import your standalone chatbot file

# --- App Config ---
st.set_page_config(
    page_title="GreenZone AI Chatbot",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items=None
)

# --- Global Gradient Background ---
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #a8edea, #fed6e3);
        background-attachment: fixed;
    }
    .main .block-container {
        background-color: rgba(255,255,255,0.85);
        border-radius: 16px;
        padding: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# --- Session State Initialization ---
if "page" not in st.session_state:
    st.session_state.page = "Login"  # Start with Login
if "is_authenticated" not in st.session_state:
    st.session_state.is_authenticated = False
if "user_name" not in st.session_state:
    st.session_state.user_name = None

# --- Routing ---
current_page = st.session_state.page

# --- Auth Gate ---
if not st.session_state.is_authenticated:
    # Always show Login page first (no header/footer here)
    auth.show()
else:
    # Show header only after login
    if current_page != "Chat":
        show_header()

    # Page rendering
    if current_page == "Home":
        home.show()
    elif current_page == "About":
        about.show()
    elif current_page == "Contact":
        contact.show()
    elif current_page == "Chat":
        mybot.show()
    else:
        home.show()  # default fallback

    # Show footer only after login (and not on Chat)
    if current_page != "Chat":
        show_footer()
