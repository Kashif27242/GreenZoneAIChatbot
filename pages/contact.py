import streamlit as st

def show():
    st.title("📩 Contact Us")
    name = st.text_input("Your Name", key="contact_name")
    email = st.text_input("Your Email", key="contact_email")
    message = st.text_area("Message", key="contact_message")
    if st.button("Send", key="contact_send"):
        st.success("✅ Message sent successfully!")
