import streamlit as st

def show():
    # --- Styles ---
    st.markdown(
        """
        <style>
        .hero {
            background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)),
                        url('https://images.unsplash.com/photo-1507525428034-b723cf961d3e') center/cover;
            padding: 100px 20px;
            text-align: center;
            border-radius: 16px;
            color: white;
        }
        .hero h1 {
            font-size: 52px;
            margin-bottom: 15px;
        }
        .hero p {
            font-size: 22px;
            opacity: 0.95;
        }
        .section {
            margin-top: 60px;
            text-align: center;
        }
        .features {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 2rem;
            margin-top: 30px;
        }
        .card {
            background: white;
            padding: 25px;
            border-radius: 14px;
            box-shadow: 0 4px 16px rgba(0,0,0,0.1);
            width: 280px;
            text-align: center;
        }
        .card h3 {
            margin-top: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # --- Hero ---
    st.markdown(
        """
        <div class="hero">
            <h1>💚 Welcome to GreenZone AI</h1>
            <p>Your AI Therapist guiding you through the GreenZone Seven Step Philosophy and the 
            Identify – Resolve – Dissolve framework.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # --- Why GreenZone ---
    st.markdown("<div class='section'><h2>🌱 Why GreenZone?</h2></div>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class="features">
            <div class="card">
                <h2>🤝</h2>
                <h3>Safe Space</h3>
                <p>Express your feelings freely — without judgment, only understanding.</p>
            </div>
            <div class="card">
                <h2>🧠</h2>
                <h3>Therapeutic Guidance</h3>
                <p>Our AI asks reflective questions to help you identify, resolve, and dissolve challenges.</p>
            </div>
            <div class="card">
                <h2>🌍</h2>
                <h3>Multilingual Support</h3>
                <p>Healing in your own language: English, Urdu, and Sindhi.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # --- Our Promise ---
    st.markdown("<div class='section'><h2>💫 Our Promise</h2></div>", unsafe_allow_html=True)
    st.markdown(
        """
        - 💚 Empathy and compassion in every response  
        - 🔒 Privacy & confidentiality at the core  
        - 🌱 Encouragement for personal growth & resilience  
        """
    )

    # --- CTA ---
    st.markdown("<div class='section'><h2>🚀 Begin Your Healing Journey</h2></div>", unsafe_allow_html=True)
    if st.button("💬 Start Talking to Your AI Therapist", key="start_chat"):
        st.session_state.page = "Chat"
        st.rerun()
