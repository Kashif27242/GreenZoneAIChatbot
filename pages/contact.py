import streamlit as st

def show():
    st.markdown(
        """
        <div style="background: linear-gradient(90deg, #2e7d32, #66bb6a);
                    padding: 20px; border-radius: 15px;
                    color: white; text-align: center; font-family: Arial;">
            <h2>📩 Contact Us</h2>
            <p>We would love to hear from you! Fill out the form below and we'll get back to you soon.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)  # spacing

    with st.form(key="contact_form"):
        name = st.text_input("Your Name", key="contact_name")
        email = st.text_input("Your Email", key="contact_email")
        message = st.text_area("Your Message", key="contact_message", height=150)

        submitted = st.form_submit_button("Send Message")
        if submitted:
            st.success("✅ Message sent successfully!")
            st.info(f"Name: {name}\nEmail: {email}\nMessage: {message}")
