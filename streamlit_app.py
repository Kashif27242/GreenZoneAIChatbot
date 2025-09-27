import streamlit as st
from components.header import show_header
from components.footer import show_footer
from pages import home, about, contact, auth
import mybot  # <-- import your standalone chatbot file

# --- App Config ---
st.set_page_config(page_title="GreenZone AI Chatbot", layout="wide" , initial_sidebar_state=None, menu_items=None)

# --- Global Gradient Background ---
st.markdown("""
    <style>
    /* Gradient for the whole app */
    .stApp {
        background: linear-gradient(135deg, #a8edea, #fed6e3);
        background-attachment: fixed;
    }
    /* Card-like content container */
    .main .block-container {
        background-color: rgba(255,255,255,0.85);
        border-radius: 16px;
        padding: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# --- Session State Initialization ---
if "page" not in st.session_state:
    st.session_state.page = "Home"
if "is_authenticated" not in st.session_state:
    st.session_state.is_authenticated = False
if "user_name" not in st.session_state:
    st.session_state.user_name = None

# --- Show Header only if NOT Chat page ---
if st.session_state.page != "Chat":
    show_header()

# --- Routing ---
current_page = st.session_state.page

# --- Authenticated check for Chat ---
if current_page == "Chat" and not st.session_state.is_authenticated:
    st.warning("⚠️ Please login first to access the Chat.")
    if st.button("Go to Login / Sign Up"):
        st.session_state.page = "Login / Sign Up"
        st.experimental_rerun()

# --- Page Rendering ---
if current_page == "Home":
    home.show()
elif current_page == "About":
    about.show()
elif current_page == "Contact":
    contact.show()
elif current_page == "Chat":
    mybot.show()  # <-- use your new chatbot file
elif current_page == "Login / Sign Up":
    auth.show()

# --- Footer only if NOT Chat page ---
if current_page != "Chat":
    show_footer()
