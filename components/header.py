import streamlit as st

def show_header():
    # --- Initialize page state ---
    if "page" not in st.session_state:
        st.session_state.page = "Home"

    # --- Fixed Menu Items ---
    menu_items = ["Home", "About", "Contact", "Chat", "Login / Sign Up"]

    # --- CSS Styling ---
    st.markdown("""
        <style>
        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 15px 40px;
            background-color: #f5f9f8;
            border-bottom: 1px solid #e0e0e0;
            box-shadow: 0 3px 10px rgba(0,0,0,0.05);
            position: sticky;
            top: 0;
            z-index: 999;
        }
        .header .logo img {
            height: 55px;
        }
        .header .menu {
            display: flex;
            gap: 10px;
        }
        .stButton>button {
            background-color: transparent;
            border: none;
            font-size: 16px;
            font-weight: 600;
            padding: 8px 15px;
            border-radius: 8px;
            cursor: pointer;
            transition: 0.3s;
            color: #2c3e50;
        }
        .stButton>button:hover {
            background-color: #2ecc71;
            color: white;
        }
        .stButton.active>button {
            background-color: #27ae60;
            color: white;
        }
        </style>
    """, unsafe_allow_html=True)

    # --- Render header ---
    col1, col2 = st.columns([1, 3])

    # Logo
    with col1:
        st.image("https://greenzoneliving.org/_next/image/GREENZONE-LIVING.webp", width=120)

    # Menu
    with col2:
        menu_cols = st.columns(len(menu_items))
        for idx, item in enumerate(menu_items):
            btn_placeholder = menu_cols[idx].empty()
            if btn_placeholder.button(item, key=f"menu_{item}"):
                st.session_state.page = item
            # Highlight active button
            if st.session_state.page == item:
                btn_placeholder.markdown(
                    f"<div class='stButton active'><button>{item}</button></div>",
                    unsafe_allow_html=True
                )

    return st.session_state.page
