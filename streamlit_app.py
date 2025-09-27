import streamlit as st
from components.header import show_header
from pages import home, about, contact, chat, auth

# --- App Config ---
st.set_page_config(page_title="GreenZone AI Chatbot", layout="wide")

# --- Session State ---
if "page" not in st.session_state:
    st.session_state.page = "Home"
if "is_authenticated" not in st.session_state:
    st.session_state.is_authenticated = False
if "user_name" not in st.session_state:
    st.session_state.user_name = None

# --- Header ---
show_header()

# --- Routing ---
if st.session_state.page == "Home":
    home.show()
elif st.session_state.page == "About":
    about.show()
elif st.session_state.page == "Contact":
    contact.show()
elif st.session_state.page == "Chat":
    chat.show()
elif st.session_state.page == "Login / Sign Up":
    auth.show()
