import streamlit as st

def show():
    # --- Styles ---
    st.markdown(
        """
        <style>
        .about-header {
            text-align: center;
            margin-bottom: 40px;
        }
        .about-header h1 {
            font-size: 42px;
            color: #2c3e50;
        }
        .about-header p {
            font-size: 18px;
            color: #555;
            max-width: 800px;
            margin: auto;
        }
        .scroll-gallery {
            display: flex;
            overflow-x: auto;
            gap: 16px;
            padding: 20px 0;
        }
        .scroll-gallery img {
            height: 180px;
            border-radius: 12px;
            flex-shrink: 0;
            box-shadow: 0 3px 10px rgba(0,0,0,0.15);
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # --- Header ---
    st.markdown(
        """
        <div class="about-header">
            <h1>🌿 About GreenZone AI</h1>
            <p>
            GreenZone AI is your digital companion for mental well-being. 
            Guided by the <b>GreenZone Seven Step Philosophy</b> and the 
            <b>Identify, Resolve, and Dissolve</b> methodology, 
            our chatbot helps individuals manage challenges in a structured way.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # --- Two Columns ---
    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.subheader("✨ Our Vision")
        st.write("""
        We aim to create a safe, accessible, and stigma-free space where 
        individuals can explore their feelings and find clarity.  
        
        Unlike typical mental health apps, GreenZone focuses on **self-problem management** —
        empowering users to navigate their challenges step by step.
        """)

        st.subheader("💡 What Makes Us Unique")
        st.write("""
        - Based on a proven therapeutic framework  
        - AI-driven guidance with empathy  
        - Multilingual support (English, Urdu, Sindhi)  
        - Privacy and confidentiality by design  
        """)

    with col2:
        st.image(
            "https://images.unsplash.com/photo-1508780709619-79562169bc64",
            use_container_width=True,
            caption="Your safe space for healing"
        )

    # --- Image Scroller ---
    st.markdown("<h3 style='margin-top:40px;'>📸 Our Journey in Pictures</h3>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class="scroll-gallery">
            <img src="https://images.unsplash.com/photo-1517245386807-bb43f82c33c4" />
            <img src="https://images.unsplash.com/photo-1522202176988-66273c2fd55f" />
            <img src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e" />
            <img src="https://images.unsplash.com/photo-1515168833906-d2a3b82b302a" />
            <img src="https://images.unsplash.com/photo-1504593811423-6dd665756598" />
        </div>
        """,
        unsafe_allow_html=True
    )
