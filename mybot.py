import streamlit as st
from google import genai
import json
import os
import uuid
from components.header import show_header 

# --- Config ---
CHAT_DIR = "chat_data"
os.makedirs(CHAT_DIR, exist_ok=True)

# --- Gemini API Client ---
client = genai.Client(api_key="AIzaSyBfmdkclHwh3-KEwpPeiVEZJSxSy59EbF0")


# --- Helper Functions ---
def user_chat_file(username):
    return os.path.join(CHAT_DIR, f"{username}_chats.json")

def load_chats(username):
    if os.path.exists(user_chat_file(username)):
        with open(user_chat_file(username), "r", encoding="utf-8") as f:
            return json.loads(f.read().strip() or "[]")
    return []

def save_chats(username, chats):
    with open(user_chat_file(username), "w", encoding="utf-8") as f:
        json.dump(chats, f, ensure_ascii=False, indent=2)

def get_current_chat(username):
    if "current_chat_id" not in st.session_state:
        chats = load_chats(username)
        st.session_state.current_chat_id = chats[-1]["id"] if chats else None
    return st.session_state.current_chat_id

def get_chat_by_id(username, chat_id):
    chats = load_chats(username)
    for chat in chats:
        if chat["id"] == chat_id:
            return chat
    return None

def update_chat(username, chat_id, messages):
    chats = load_chats(username)
    for chat in chats:
        if chat["id"] == chat_id:
            chat["messages"] = messages
    save_chats(username, chats)


# --- Main Chat UI ---
def show():
    show_header()
    if not st.session_state.is_authenticated:
        st.warning("⚠️ You must login first to access the Chat.")
        if st.button("Go to Login / Sign Up", key="chat_login_btn"):
            st.session_state.page = "Login / Sign Up"
            st.rerun()
        return

    username = st.session_state.user_name
    chats = load_chats(username)

    # --- Sidebar + Main Layout ---
    col_sidebar, col_chat = st.columns([1, 3])

    with col_sidebar:
        st.markdown("### 📂 Your Chats")
        
        # New Chat
        if st.button("➕ New Chat", key="new_chat_btn"):
            new_chat = {
                "id": str(uuid.uuid4()),
                "title": f"Chat {len(chats)+1}",
                "messages": []
            }
            chats.append(new_chat)
            save_chats(username, chats)
            st.session_state.current_chat_id = new_chat["id"]
            st.rerun()

        st.markdown("---")
        # Scrollable chat list
        for chat in chats:
            first_msg = chat["messages"][0]["content"][:30] + ("..." if len(chat["messages"][0]["content"]) > 30 else "") if chat["messages"] else chat["title"]
            col1, col2 = st.columns([4, 1])
            with col1:
                if st.button(first_msg, key=f"chat_{chat['id']}"):
                    st.session_state.current_chat_id = chat["id"]
                    st.rerun()
            with col2:
                if st.button("🗑️", key=f"del_{chat['id']}"):
                    chats = [c for c in chats if c["id"] != chat["id"]]
                    save_chats(username, chats)
                    if st.session_state.get("current_chat_id") == chat["id"]:
                        st.session_state.current_chat_id = chats[-1]["id"] if chats else None
                    st.rerun()

        st.markdown("---")
        st.markdown("### ⚙️ Chat Settings")
        mode = st.radio("Mode", ["Therapist", "Learner", "Motivator"], key="mode_select")
        language = st.selectbox("Language", ["English", "Urdu", "Sindhi"], key="lang_select")
        custom_instructions = st.text_area("Custom Instructions", key="instructions_input")

        if st.button("⬅️ Back to Home", key="back_to_home"):
            st.session_state.page = "Home"
            st.rerun()

    # --- Main Chat Area ---
    with col_chat:
        st.markdown(
            """
            <div style="background: linear-gradient(90deg, #2e7d32, #66bb6a);
                        padding:15px; border-radius:12px; margin-bottom:15px;
                        color:white; text-align:center; font-size:18px;
                        font-family:Arial;">
                🌱 <b>Green Zone AI</b><br>
                <i>"Helping you grow with positivity and wisdom."</i>
            </div>
            """,
            unsafe_allow_html=True
        )

        current_chat_id = get_current_chat(username)
        if not current_chat_id:
            st.info("Start a new chat from the sidebar.")
            return

        current_chat = get_chat_by_id(username, current_chat_id)
        if "messages" not in current_chat:
            current_chat["messages"] = []

        # Chat CSS
        st.markdown(
            """
            <style>
            .chat-container {
                background-color: #f7f9f8;
                padding: 20px;
                border-radius: 16px;
                max-width: 900px;
                margin: auto;
                box-shadow: 0 4px 12px rgba(0,0,0,0.08);
                height: 70vh;
                overflow-y: auto;
            }
            .user-msg {
                color: #0d47a1;
                background-color: #e3f2fd;
                padding: 10px 15px;
                border-radius: 12px;
                margin: 5px 0;
                display: inline-block;
                max-width: 80%;
            }
            .bot-msg {
                color: #1b5e20;
                background-color: #e8f5e9;
                padding: 10px 15px;
                border-radius: 12px;
                margin: 5px 0;
                display: inline-block;
                max-width: 80%;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

      

        for msg in current_chat["messages"]:
            if msg["role"] == "user":
                st.markdown(f'<div class="user-msg"><b>You:</b> {msg["content"]}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="bot-msg"><b>AI:</b> {msg["content"]}</div>', unsafe_allow_html=True)

        # Chat input with Enter key submission
        user_input = st.text_input("💭 Type your message...", key=f"chat_input_{current_chat_id}", on_change=lambda: st.session_state.__setitem__("submit_flag", True))
        if st.session_state.get("submit_flag") and user_input:
            st.session_state["submit_flag"] = False
            current_chat["messages"].append({"role": "user", "content": user_input})

            prompt = f"""
            You are in {mode} mode.
            Language: {language}.
            Follow these custom instructions: {custom_instructions}.
            User said: {user_input}
            """

            try:
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=[prompt]
                )
                bot_reply = response.candidates[0].content.parts[0].text
            except Exception as e:
                bot_reply = f"⚠️ Error: {str(e)}"

            current_chat["messages"].append({"role": "assistant", "content": bot_reply})
            update_chat(username, current_chat_id, current_chat["messages"])
            st.rerun()
        

        st.markdown('</div>', unsafe_allow_html=True)
