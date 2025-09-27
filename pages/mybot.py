import streamlit as st
from google import genai
import json
import os

# --- Config ---
CHAT_DIR = "chat_data"
os.makedirs(CHAT_DIR, exist_ok=True)

# --- Gemini API Client ---
client = genai.Client(api_key="AIzaSyBfmdkclHwh3-KEwpPeiVEZJSxSy59EbF0")

# --- Helper Functions ---
def user_chat_file(username):
    return os.path.join(CHAT_DIR, f"{username}.json")

def load_history(username):
    if os.path.exists(user_chat_file(username)):
        with open(user_chat_file(username), "r", encoding="utf-8") as f:
            data = f.read().strip()
            return json.loads(data) if data else []
    return []

def save_history(username, history):
    with open(user_chat_file(username), "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=2)


# --- Main Chat UI ---
def show():
    # --- Authentication Check ---
    if not st.session_state.is_authenticated:
        st.warning("⚠️ You must login first to access the Chat.")
        if st.button("Go to Login / Sign Up"):
            st.session_state.page = "Login / Sign Up"
            st.rerun()
        return

    username = st.session_state.user_name
    if "messages" not in st.session_state:
        st.session_state.messages = load_history(username)

    # --- Layout with Custom Sidebar ---
    left, right = st.columns([1, 3])

    # ---------------- Sidebar (Left Column) ----------------
    with left:
        st.markdown("### 📂 Chat History")

        # Load existing history
        chat_history = load_history(username)

        if chat_history:
            for i, msg in enumerate(chat_history):
                if msg["role"] == "user":
                    if st.button(f"📝 Chat {i+1}", key=f"history_{i}"):
                        # Load from selected point
                        st.session_state.messages = chat_history[: i + 1]
                        st.rerun()

            if st.button("🗑️ Clear All History"):
                st.session_state.messages = []
                save_history(username, [])
                st.rerun()
        else:
            st.info("No chat history yet.")

        st.markdown("---")
        st.markdown("### ⚙️ Chat Settings")

        mode = st.radio("Mode", ["Therapist", "Learner", "Motivator"])
        language = st.selectbox("Language", ["English", "Urdu", "Sindhi"])
        custom_instructions = st.text_area("Custom Instructions")

        if st.button("⬅️ Back to Home"):
            st.session_state.page = "Home"
            st.rerun()

    # ---------------- Main Chat Area (Right Column) ----------------
    with right:
        st.markdown(
            """
            <style>
            .chat-container {
                background-color: #f7f9f8;
                padding: 20px;
                border-radius: 16px;
                max-width: 900px;
                margin: auto;
                box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            }
            .user-msg {
                color: #0d47a1;
                background-color: #e3f2fd;
                padding: 10px 15px;
                border-radius: 12px;
                margin: 5px 0;
                display: inline-block;
            }
            .bot-msg {
                color: #1b5e20;
                background-color: #e8f5e9;
                padding: 10px 15px;
                border-radius: 12px;
                margin: 5px 0;
                display: inline-block;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        st.markdown('<div class="chat-container">', unsafe_allow_html=True)

        # Display history
        for msg in st.session_state.messages:
            if msg["role"] == "user":
                st.markdown(f'<div class="user-msg"><b>You:</b> {msg["content"]}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="bot-msg"><b>AI:</b> {msg["content"]}</div>', unsafe_allow_html=True)

        # Input
        user_input = st.text_input("💭 Type your message...", key="chat_input")
        if st.button("Send", key="send_btn") and user_input:
            st.session_state.messages.append({"role": "user", "content": user_input})

            prompt = f"""
            You are in {mode} mode.
            Language: {language}.
            Follow these custom instructions: {custom_instructions}.
            User said: {user_input}
            """

            # Generate response
            try:
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=[prompt]
                )
                bot_reply = response.candidates[0].content.parts[0].text
            except Exception as e:
                bot_reply = f"⚠️ Error: {str(e)}"

            st.session_state.messages.append({"role": "assistant", "content": bot_reply})
            save_history(username, st.session_state.messages)
            st.rerun()

        st.markdown('</div>', unsafe_allow_html=True)
