import streamlit as st
from styles import apply_custom_styles
from engine import run_welfare_detection
from form import render_intelligent_form
from connect import render_connect_page
from pdf_gen import create_pdf

# ---------------------------------------------------------
# GLOBAL CONFIGURATION
# ---------------------------------------------------------
st.set_page_config(page_title="Schemo", page_icon="🛡️", layout="wide")
apply_custom_styles()


# Add Sidebar Banner
with st.sidebar:
    st.image("logo.png", use_container_width=True)
   # st.markdown("---")

# ---------------------------------------------------------
# SIDEBAR NAVIGATION
# ---------------------------------------------------------
if "nav_selection" not in st.session_state:
    st.session_state.nav_selection = "Home"

st.sidebar.title("🛡️ Schemo")
st.sidebar.markdown("---")
menu = st.sidebar.radio(
    "Navigate", 
    ["Home", "Detect & Guide", "Connect (Maps)", "Track History (Status)"], key="nav_selection"
)
def switch_to_detect():
    st.session_state.nav_selection = "Detect & Guide"

# ---------------------------------------------------------
# PAGE: HOME
# ---------------------------------------------------------
if menu == "Home":

    # 1. Display the banner on Top
    st.image("banner.png", use_container_width=True)

    st.title("Welcome to Schemo 🇮🇳")
    st.markdown("""
    ### Bridging the gap between Citizens and Welfare.
    Millions of eligible citizens miss out on government benefits simply because they don't know they exist. 
    **Schemo** uses AI to change that.
    """)
    st.button("Start Eligibility Check 🚀", on_click=switch_to_detect)

    # Demo Video
    st.markdown("---")
    st.subheader("📺 See How It Works (Demo Video)")
    
    st.video("https://youtu.be/r7gTAwMdliw?si=VhkZcXxKaUdVHMUF")
   
# ---------------------------------------------------------
# PAGE: DETECT & GUIDE
# ---------------------------------------------------------
elif menu == "Detect & Guide":
    st.title("🔍 Eligibility Detection Engine")
    
    user_profile_string = render_intelligent_form()

    if user_profile_string:
        st.success("✅ Profile Built Successfully!")
        with st.spinner("🤖 AI is cross-referencing schemes..."):
            try:
                ai_results = run_welfare_detection(user_profile_string)
                
                st.session_state['stored_results'] = ai_results
                
            except Exception as e:
                st.error(f"Error: {e}")

    if 'stored_results' in st.session_state:
        
        
        final_output = st.session_state['stored_results']
        # -----------------------------------------------------
        # PDF DOWNLOAD BUTTON
        # -----------------------------------------------------
        col_head1, col_head2 = st.columns([3, 1])
        with col_head1:
            st.subheader("📋 Your Personalized Benefit Report")
        with col_head2:
            
            user_inputs = f"Occupation: {st.session_state.get('occupation_selector', 'N/A')}, State: {st.session_state.get('p_state', 'N/A')}"
            
            pdf_bytes = create_pdf(final_output)
            
            st.download_button(
                label="📥 Download PDF",
                data=pdf_bytes,
                file_name="Schemo_Report.pdf",
                mime="application/pdf"
            )
        # -----------------------------------------------------

        
        st.markdown("---")
        st.subheader("📋 Your Personalized Benefit Report")
        
        # Display Logic (Card View)
        schemes = final_output.split("---")
        if len(schemes) > 1:
            for scheme in schemes:
                if len(scheme.strip()) > 10:
                    with st.container():
                        st.info(scheme.strip())
                        col1, col2 = st.columns([4, 1])
                        col1.write("✅ Eligibility Confirmed")
        else:
            with st.container():
                st.markdown(final_output)
                st.link_button("Go to Official Portal 🔗", "https://www.india.gov.in/")
        
        st.markdown("---")
        # Reset button
        if st.button("🔄 Reset Analysis"):
            del st.session_state['stored_results']
            st.rerun()

# ---------------------------------------------------------
# PAGE: CONNECT (Maps)
# ---------------------------------------------------------
elif menu == "Connect (Maps)":
    if 'user_state_selection' in st.session_state:
        render_connect_page(st.session_state['user_state_selection'])
    else:
        st.warning("⚠️ Please fill the 'Detect' form first so we know your State!")
        render_connect_page() 

# ---------------------------------------------------------
# PAGE: TRACK HISTORY
# ---------------------------------------------------------
elif menu == "Track History":
    st.title("📜 Application History")
    st.info("Coming Soon: Save your recommended schemes here.")


# code written by- Shivansh
