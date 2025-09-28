import streamlit as st

def show():
       # --- Header Banner ---
    st.markdown(
        """
        <div style="background: linear-gradient(90deg, #2e7d32, #66bb6a);
                    padding: 25px; border-radius: 15px;
                    color: white; text-align: center; font-family: Arial;">
            <h2>🔑 Welcome to GreenZone AI</h2>
            <p>Login or create a new account to continue your journey with us.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.title("🔑 Login / Sign Up")

    tab1, tab2 = st.tabs(["Login", "Sign Up"])

    with tab1:
        email = st.text_input("Email", key="login_email")
        password = st.text_input("Password", type="password", key="login_password")
        if st.button("Login", key="login_btn"):
            if email and password:
                st.session_state.is_authenticated = True
                st.session_state.user_name = email.split("@")[0].title()
                st.success(f"✅ Logged in as {st.session_state.user_name}")
            else:
                st.error("❌ Enter email & password")

    with tab2:
        first_name = st.text_input("First Name", key="signup_first_name")
        last_name = st.text_input("Last Name", key="signup_last_name")
        new_email = st.text_input("Email", key="signup_email")
        new_pass = st.text_input("Password", type="password", key="signup_password")
        if st.button("Sign Up", key="signup_btn"):
            if first_name and last_name and new_email and new_pass:
                st.success("🎉 Account created! Please login.")
            else:
                st.error("❌ Fill all fields")
