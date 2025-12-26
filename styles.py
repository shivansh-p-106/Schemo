import streamlit as st

def apply_custom_styles():
    st.markdown("""
        <style>
        /* 1. IMPORT FONT */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');
        
        /* 2. GLOBAL RESET */
        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
            color: #e2e8f0;
        }

        /* 3. APP BACKGROUND */
        .stApp {
            /* Main gradient for the body */
            background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%);
            background-attachment: fixed;
        }
        
        /* 4. SOLID COLORED HEADER */
        header[data-testid="stHeader"] {
            background-color: #1e293b !important; /* Solid Dark Slate */
            border-bottom: 1px solid #334155; /* Thin separation line */
            z-index: 999; /* Ensure it sits on top */
        }
        
        .block-container {
            background-color: transparent !important;
        }

        /* 5. CARD STYLING */
        div[data-testid="stAlert"] {
            background-color: rgba(30, 41, 59, 0.8) !important;
            border: 1px solid #334155 !important;
            border-left: 5px solid #06b6d4 !important; /* Cyan accent */
            color: #f1f5f9 !important;
            border-radius: 10px;
            padding: 1.2rem;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.3);
            transition: all 0.2s ease;
        }
        
        div[data-testid="stAlert"]:hover {
            transform: translateY(-3px);
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.4);
            border-left-color: #22d3ee !important;
        }

        /* 6. BUTTONS */
        div.stButton > button {
            width: 100%;
            background: linear-gradient(90deg, #3b82f6 0%, #2563eb 100%);
            color: white;
            font-weight: 600;
            border: none;
            padding: 0.75rem 1rem;
            border-radius: 8px;
            transition: all 0.3s ease;
        }

        div.stButton > button:hover {
            background: linear-gradient(90deg, #2563eb 0%, #1d4ed8 100%);
            transform: scale(1.02);
            box-shadow: 0 0 15px rgba(59, 130, 246, 0.5);
        }

        /* 7. INPUTS & HEADERS */
        .stTextInput > div > div > input, 
        .stSelectbox > div > div > div, 
        .stTextArea > div > div > textarea {
            background-color: #1e293b !important;
            color: #f8fafc !important;
            border: 1px solid #475569 !important;
            border-radius: 8px;
        }

        h1, h2, h3, label {
            color: #f8fafc !important;
        }
        
        label {
            color: #cbd5e1 !important;
        }
                
        /* 8. MAKE BOLD LABELS WHITE */
        div[data-testid="stAlert"] strong {
        color: #ffffff !important; /* Pure White */
        font-weight: 700 !important;
}
        </style>
    """, unsafe_allow_html=True)