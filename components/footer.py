import streamlit as st

def show_footer():
    st.markdown(
        """
        <style>
        .footer {
            background: url('https://greenzoneliving.org/_next/static/media/footer-bg.ccfbc3bd.png') center/cover no-repeat;
            color: white;
            padding: 30px 20px;
            text-align: center;
            border-radius: 12px;
            font-size: 14px;
        }
        .footer a {
            color: white;
            text-decoration: none;
        }
        .footer a:hover {
            text-decoration: underline;
        }
        </style>

        <div class="footer">
            <p>💚 GREENZONE LIVING – Inspiring peaceful and mindful living.</p>
            <p>
                🌐 <a href="#">Blog</a> | <a href="#">Donate</a> | <a href="#">About</a> | 
                <a href="#">Resources</a> | <a href="#">Disclaimer</a>
            </p>
            <p>📧 greenzonelifestyle@gmail.com | 📍 213 Byron Street South, Whitby, ON, Canada</p>
        </div>
        """,
        unsafe_allow_html=True
    )
