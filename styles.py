import streamlit as st

def apply_custom_css():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');
        
        /* Typography and Colors */
        html, body, [class*="css"]  {
            font-family: 'Inter', sans-serif;
            color: #E2E8F0;
            background-color: #0F172A;
        }
        
        /* Main background - subtle gradient */
        .stApp {
            background: radial-gradient(circle at 10% 20%, rgb(15, 23, 42) 0%, rgb(30, 41, 59) 90%);
        }

        /* Glassmorphism for containers and elements */
        div[data-testid="stVerticalBlock"] > div[data-testid="stVerticalBlock"] {
            background: rgba(30, 41, 59, 0.4);
            border-radius: 16px;
            padding: 20px;
            box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        /* Headers */
        h1, h2, h3 {
            color: #38BDF8 !important;
            font-weight: 800 !important;
        }
        h1 {
            background: -webkit-linear-gradient(45deg, #38BDF8, #818CF8);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        /* Buttons */
        .stButton>button {
            background: linear-gradient(135deg, #38BDF8 0%, #3B82F6 100%);
            color: white;
            border-radius: 8px;
            border: none;
            padding: 10px 24px;
            font-weight: 600;
            transition: all 0.3s ease;
        }
        .stButton>button:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 20px rgba(56, 189, 248, 0.4);
            color: white;
        }

        /* Alerts/Banners Customization */
        .stAlert {
            border-radius: 12px;
            border: none;
            backdrop-filter: blur(10px);
        }
        
        div[data-testid="stExpander"] {
            background: rgba(15, 23, 42, 0.6);
            border-radius: 10px;
            border: 1px solid rgba(56, 189, 248, 0.2);
        }
        
        /* Sidebar styling */
        [data-testid="stSidebar"] {
            background-color: rgba(15, 23, 42, 0.8) !important;
            backdrop-filter: blur(15px);
            border-right: 1px solid rgba(255, 255, 255, 0.1);
        }
        </style>
    """, unsafe_allow_html=True)
