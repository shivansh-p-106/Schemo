import streamlit as st
from google import genai
from google.genai import types

# ---------------------------------------------------------
# CLIENT SETUP
# ---------------------------------------------------------
def get_ai_client():
    try:
        # Fetch the key securely from Streamlit secrets
        api_key = st.secrets["GOOGLE_API_KEY"]
        return genai.Client(api_key=api_key)
    except Exception as e:
        st.error(f"🚨 Connection Error: {e}")
        return None

# ---------------------------------------------------------
# CORE ENGINE LOGIC
# ---------------------------------------------------------
def run_welfare_detection(user_profile):
    client = get_ai_client()
    if not client:
        return "System Error: API Key not found."

    # -----------------------------------------------------
    # PROMPT ENGINEERING
    # -----------------------------------------------------
    
    system_instruction = """
    You are a Senior Government Welfare Officer in India.(don't mention this in your response; just for your understanding) 
    Your goal is to identify the **Top 5 most relevant active welfare schemes** for a citizen based on their profile.
    
    CRITICAL RULES:
    1. Output MUST be in clean Markdown format with bullet points.
    2. Only suggest schemes that are currently ACTIVE.
    3. Clearly state who runs the scheme (State vs Center).
    4. Provide specific documents required (e.g., Aadhaar, Income Cert).
    5. You MUST use the separator '---' between schemes.
    """

    prompt = f"""
    Analyze this citizen profile:
    {user_profile}

    Identify the **Top 5 Welfare Schemes** they are most likely eligible for.
    
    Format each scheme EXACTLY like this template:
    
    ### [Scheme Name]
    * **Run By:** [State Govt / Central Govt]
    * **Benefit:** [Clear summary of financial/social benefit]
    * **Why You Qualify:** [Specific reason based on their data, e.g. "Income < 1.5L"]
    * **Required Documents:** [List 3-4 key documents in bullets]
    * **How to Apply:** [Brief step-by-step or specific portal name]
    * **Video Guide:** [Construct a URL exactly like this: https://www.youtube.com/results?search_query=how+to+apply+for+[Scheme Name]]
    * **Official Link:** [Direct URL]
    
    ---
    
    (Repeat for Scheme 2, 3, 4, 5)
    """

    models_to_try = ["models/gemini-2.5-flash", "models/gemini-2.0-flash"]
    
    for model_id in models_to_try:
        try:
            response = client.models.generate_content(
                model=model_id,
                contents=prompt,
                config=types.GenerateContentConfig(
                    system_instruction=system_instruction,
                    temperature=0.3  # Low temperature for factual accuracy
                )
            )
            return response.text

        except Exception as e:
            if model_id == models_to_try[-1]:
                return f"⚠️ Service Busy: {str(e)}. Please try again in 60 seconds."
            continue