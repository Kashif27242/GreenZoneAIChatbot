import streamlit as st
import os
import json
from google import genai
from google.genai import types

# --------------------------
# Config
# --------------------------
CHAT_DIR = "test_user_data"
os.makedirs(CHAT_DIR, exist_ok=True)

# Initialize Gemini client
client = genai.Client(api_key=st.secrets.get("GEMINI_API_KEY", "AIzaSyBfmdkclHwh3-KEwpPeiVEZJSxSy59EbF0"))

# --------------------------
# Helper functions
# --------------------------
def user_chat_file(user="demo_user"):
    return os.path.join(CHAT_DIR, f"{user}.json")

def load_history(user="demo_user"):
    if os.path.exists(user_chat_file(user)):
        with open(user_chat_file(user), "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_history(user, history):
    with open(user_chat_file(user), "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=2)

# --------------------------
# Streamlit UI
# --------------------------
st.title("💬 Test Gemini Flash Chat")
st.caption("Standalone testing environment")

# Sidebar options
mode = st.sidebar.radio("Mode", ["Therapist", "Learner", "Motivator"])
language = st.sidebar.selectbox("Language", ["English", "Urdu", "Sindhi"])
custom_instructions = st.sidebar.text_area("Custom Instructions (Optional)")

uploaded_file = st.sidebar.file_uploader("📄 Upload Document", type=["txt", "md", "pdf"])
doc_content = None
if uploaded_file:
    if uploaded_file.type == "application/pdf":
        doc_data = uploaded_file.read()
        doc_content = types.Part.from_bytes(data=doc_data, mime_type="application/pdf")
    else:
        doc_content = uploaded_file.read().decode("utf-8")

# Load or initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = load_history()

# User input
user_input = st.chat_input("Type your message here...")
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Build prompt
    contents = []
    if doc_content:
        contents.append(doc_content)

    prompt = f"""
You are in {mode} mode.
Language: {language}.
Custom Instructions: {custom_instructions}.
User said: {user_input}
"""
    contents.append(prompt)

    # Call Gemini Flash 2.0
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=contents
        )
        bot_reply = response.text
    except Exception as e:
        bot_reply = f"⚠️ Error calling Gemini API: {e}"

    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    save_history("demo_user", st.session_state.messages)

# Display chat history
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"<div style='color:blue;'><b>You:</b> {msg['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div style='color:green;'><b>AI:</b> {msg['content']}</div>", unsafe_allow_html=True)

# Clear chat
if st.sidebar.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    save_history("demo_user", [])
    st.rerun()
