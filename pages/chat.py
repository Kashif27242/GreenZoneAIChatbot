import streamlit as st

def show():
    st.title("💬 Chat with AI")
    if not st.session_state.is_authenticated:
        st.warning("⚠️ Please login to use the chatbot.")
        return

    user_input = st.text_input("Type your message:", key="chat_input")
    if st.button("Send", key="chat_send"):
        st.chat_message("user").write(user_input)
        st.chat_message("assistant").write("🤖 This is a demo AI response.")
