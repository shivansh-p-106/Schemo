import streamlit as st

def render_connect_page(user_state="Uttar Pradesh"): # Default to U.P. if no state selected
    
    st.title(f"📍 Locate Help Centers in {user_state}")
    st.markdown("Find your nearest **Jan Seva Kendra (CSC)** or Government Office below.")

    query = f"Common Service Center {user_state}"
    # Encoding spaces for URL
    query_url = query.replace(" ", "+")
    
    # Using Google Maps Embed API (Search Mode)
    map_html = f"""
        <div style="background-color: white; padding: 10px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
            <iframe 
                width="100%" 
                height="450" 
                frameborder="0" 
                scrolling="no" 
                marginheight="0" 
                marginwidth="0" 
                src="https://maps.google.com/maps?q={query_url}&t=&z=10&ie=UTF8&iwloc=&output=embed">
            </iframe>
        </div>
    """
    st.markdown(map_html, unsafe_allow_html=True)
    
    st.markdown("---")

    # ---------------------------------------------------------
    # STATE HELPLINE DATABASE
    # ---------------------------------------------------------
    st.subheader(f"📞 Official Helplines: {user_state}")
    
    # A mini-database of CM Helplines
    helplines = {
        "Uttar Pradesh": "1076 (CM Helpline)",
        "Bihar": "1800-345-6268 (Public Grievance)",
        "Maharashtra": "1800-120-8040 (MahaDBT)",
        "Delhi": "1031 (e-District)",
        "Karnataka": "1902 (Janaspandana)",
        "Tamil Nadu": "1100 (CM Helpline)",
        "Rajasthan": "181 (Sampark)",
        "West Bengal": "1070 / 9137091370 (Didi Ke Bolo)",
        "Odisha": "14545 (Mo Sarkar)",
        "Madhya Pradesh": "181 (CM Helpline)"
    }
    
    number = helplines.get(user_state, "1800-11-1555 (National Kisan Call Center)")
    
    col1, col2 = st.columns(2)
    with col1:
        st.info(f"**State Helpline:** {number}")
    with col2:
        st.success("**National Umang App:** 97183-97183 (WhatsApp)")

    st.caption("💡 **Pro Tip:** Visit the center between 10:00 AM - 4:00 PM for faster service.")