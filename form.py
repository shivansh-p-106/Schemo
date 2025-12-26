import streamlit as st

def render_intelligent_form():
    
    st.markdown("### 📝 Build Your Profile")
    st.info("👇 Select your occupation first to see specific questions.")
    
    # OCCUPATION SELECTOR (Outside Form)
    occ_options = [
        "Student", 
        "Farmer / Agriculturist", 
        "Daily Wage / Construction Worker",
        "Private Sector Employee", 
        "Government Employee", 
        "Business Owner / Entrepreneur",
        "Gig Worker / Freelancer",
        "Homemaker",
        "Retired / Senior Citizen",
        "Unemployed"
    ]
    saved_occ = st.session_state.get("occ_select", "Student")
    try:
        occ_index = occ_options.index(saved_occ)
    except ValueError:
        occ_index = 0

    occupation_type = st.selectbox(
        "Which category best describes you?", 
        occ_options,
        index=occ_index,
        key="occ_select"
    )

    # THE MAIN FORM
    with st.form("intelligent_welfare_form"):
        
        st.markdown("---")
        st.subheader("👤 Personal Details")
        
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Full Name", value=st.session_state.get("f_name", ""), key="f_name")
            age = st.number_input("Age", 1, 110, value=st.session_state.get("f_age", 25), key="f_age")
            
            gen_opts = ["Male", "Female", "Other"]
            gen_idx = gen_opts.index(st.session_state.get("f_gender", "Male")) if st.session_state.get("f_gender") in gen_opts else 0
            gender = st.selectbox("Gender", gen_opts, index=gen_idx, key="f_gender")

            disability = st.checkbox("Person with Disability (PwD)?", value=st.session_state.get("f_pwd", False), key="f_pwd")

        
        with col2:
            all_states = sorted([
                "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", 
                "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", 
                "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", 
                "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", 
                "Uttar Pradesh", "Uttarakhand", "West Bengal", "Andaman and Nicobar Islands", 
                "Chandigarh", "Dadra and Nagar Haveli and Daman and Diu", "Delhi", 
                "Jammu and Kashmir", "Ladakh", "Lakshadweep", "Puducherry"
            ])

            saved_state = st.session_state.get("f_state", "Uttar Pradesh")
            state_idx = all_states.index(saved_state) if saved_state in all_states else 0
            state = st.selectbox("State/UT", all_states, index=state_idx, key="f_state")
            
            caste_opts = ["General", "OBC", "SC", "ST", "EWS"]
            caste_idx = caste_opts.index(st.session_state.get("f_caste", "General")) if st.session_state.get("f_caste") in caste_opts else 0
            caste = st.selectbox("Category", caste_opts, index=caste_idx, key="f_caste")

            status_opts = ["None", "Unmarried", "Married", "Widowed (Female)", "Divorced"]
            status_idx = status_opts.index(st.session_state.get("f_status", "None")) if st.session_state.get("f_status") in status_opts else 0
            status = st.selectbox("Marital Status", status_opts, index=status_idx, key="f_status")

            

        st.markdown("---")
        
        # LOGIC BRANCHING: Occupation specific questions
        st.subheader(f"💼 Details for: {occupation_type}")
        specific_details = "None"
        
        # BRANCH 1: STUDENT
        if occupation_type == "Student":
            st.success("🎓 Specific questions for Students")
            sc1, sc2 = st.columns(2)
            lvl_opts = ["School (1-10)", "High School (11-12)", "Diploma/ITI", "Undergraduate", "Postgraduate", "PhD"]
            lvl_idx = lvl_opts.index(st.session_state.get("s_level", lvl_opts[0])) if st.session_state.get("s_level") in lvl_opts else 0
            
            level = sc1.selectbox("Current Level", lvl_opts, index=lvl_idx, key="s_level")
            stream = sc2.text_input("Stream (e.g., Arts, Science)", value=st.session_state.get("s_stream", ""), key="s_stream")
            specific_details = f"Education: {level}, Stream: {stream}"

        # BRANCH 2: FARMER
        elif occupation_type == "Farmer / Agriculturist":
            st.success("🌾 Specific questions for Farmers") 
            fc1, fc2 = st.columns(2)
            land_size = fc1.number_input("Land Size (in Hectares)", 0.0, 100.0, value=st.session_state.get("fa_land", 1.0), key="fa_land")
            
            own_opts = ["Owner", "Tenant", "Sharecropper"]
            own_idx = own_opts.index(st.session_state.get("fa_type", "Owner")) if st.session_state.get("fa_type") in own_opts else 0
            land_owner = fc2.radio("Ownership Type", own_opts, index=own_idx, key="fa_type")
            
            kcc = st.checkbox("Do you have a Kisan Credit Card?", value=st.session_state.get("fa_kcc", False), key="fa_kcc")
            pm_kisan = st.checkbox("Are you receiving PM-Kisan?", value=st.session_state.get("fa_pm", False), key="fa_pm")
            specific_details = f"Land: {land_size} Ha, Type: {land_owner}, KCC: {kcc}, PM-Kisan Active: {pm_kisan}"

        # BRANCH 3: DAILY WAGE
        elif occupation_type == "Daily Wage / Construction Worker":
            st.success("🏗️ Specific questions for Workers")
            wc1, wc2 = st.columns(2)
            
            card_opts = ["e-Shram Card", "Labor Card", "None"]
            card_idx = card_opts.index(st.session_state.get("dw_card", "None")) if st.session_state.get("dw_card") in card_opts else 0
            card_type = wc1.selectbox("Worker Card", card_opts, index=card_idx, key="dw_card")
            
            mgnrega = wc2.checkbox("Worked under MGNREGA (100 Days)?", value=st.session_state.get("dw_mgn", False), key="dw_mgn")
            specific_details = f"Card: {card_type}, MGNREGA: {mgnrega}"

        # BRANCH 4: RETIRED
        elif occupation_type == "Retired / Senior Citizen":
            st.success("👴 Specific questions for Senior Citizens")
            # Radio index logic (0=Yes, 1=No)
            pen_idx = 0 if st.session_state.get("ret_pen", "No") == "Yes" else 1
            pension = st.radio("Are you receiving any pension?", ["Yes", "No"], index=pen_idx, key="ret_pen")
            specific_details = f"Pension Status: {pension}"

        # BRANCH 5: BUSINESS
        elif occupation_type == "Business Owner / Entrepreneur":
            st.success("🚀 Specific questions for Business")
            bc1, bc2 = st.columns(2)
            
            biz_opts = ["Street Vendor", "Small Shop", "MSME/Factory"]
            biz_idx = biz_opts.index(st.session_state.get("biz_type", biz_opts[0])) if st.session_state.get("biz_type") in biz_opts else 0
            biz_type = bc1.selectbox("Business Type", biz_opts, index=biz_idx, key="biz_type")
            
            loan = bc2.checkbox("Interested in Mudra Loan?", value=st.session_state.get("biz_loan", False), key="biz_loan")
            specific_details = f"Business: {biz_type}, Wants Loan: {loan}"
            
        # BRANCH 6: HOMEMAKER
        elif occupation_type == "Homemaker":
            st.success("🏠 Specific questions for Homemakers")
            shg_idx = 0 if st.session_state.get("home_shg", "No") == "Yes" else 1
            shg = st.radio("Member of Self-Help Group (SHG)?", ["Yes", "No"], index=shg_idx, key="home_shg")
            specific_details = f"SHG Member: {shg}"

        # BRANCH 7: PRIVATE EMPLOYEE
        elif occupation_type == "Private Sector Employee":
            st.success("🏢 Private Sector Details")
            epf_idx = 0 if st.session_state.get("pvt_epf", "No") == "Yes" else 1
            epf = st.radio("Is EPF deducted?", ["Yes", "No"], index=epf_idx, key="pvt_epf")
            specific_details = f"Private Job, EPF: {epf}"

        # BRANCH 8: GOVERNMENT EMPLOYEE
        elif occupation_type == "Government Employee":
            st.success("🏛️ Govt Service Details")
            gov_opts = ["Central", "State", "PSU"]
            gov_idx = gov_opts.index(st.session_state.get("gov_lvl", gov_opts[0])) if st.session_state.get("gov_lvl") in gov_opts else 0
            level = st.selectbox("Level", gov_opts, index=gov_idx, key="gov_lvl")
            specific_details = f"Govt Job Level: {level}"

        # BRANCH 9: GIG WORKER
        elif occupation_type == "Gig Worker / Freelancer":
            st.success("🛵 Gig Economy Details")
            plat = st.text_input("Platform Name (e.g. Swiggy, Uber)", value=st.session_state.get("gig_plat", ""), key="gig_plat")
            specific_details = f"Platform: {plat}"

        # FALLBACK
        else:
            st.info("ℹ️ Providing general details helps accuracy.")
            skill = st.text_input("Any specific technical skill?", value=st.session_state.get("gen_skill", ""), key="gen_skill")
            specific_details = f"Skill: {skill}"

        st.markdown("---")
        
        # ECONOMIC STATUS
        st.subheader("💰 Economic Status")
        
        ec1, ec2, ec3 = st.columns(3)
        with ec1:
            income = st.number_input("Annual Family Income (₹)", 0, 10000000, value=st.session_state.get("eco_inc", 80000), step=5000, key="eco_inc")
        with ec2:
            rat_opts = ["None", "APL (Above Poverty Line)", "BPL (Below Poverty Line)", "AAY (Antyodaya/Poorest)"]
            rat_idx = rat_opts.index(st.session_state.get("eco_rat", rat_opts[0])) if st.session_state.get("eco_rat") in rat_opts else 0
            ration_card = st.selectbox("Ration Card Type", rat_opts, index=rat_idx, key="eco_rat")
        with ec3:
            house_opts = ["Own Pucca House", "Kucha/Mud House", "Rented", "Homeless / No Shelter"]
            house_idx = house_opts.index(st.session_state.get("eco_house", house_opts[0])) if st.session_state.get("eco_house") in house_opts else 0
            housing_type = st.selectbox("Current Housing Type", house_opts, index=house_idx, key="eco_house")
        
        # SUBMIT
        submitted = st.form_submit_button("🔍 Run AI Eligibility Check")

    if submitted:
        st.session_state['user_state_selection'] = state
        
        profile_string = (
            f"User Profile: {age} yr old {gender}, {occupation_type} in {state}. "
            f"Category: {caste}. Disability: {disability}. "
            f"Specifics: [{specific_details}]. "
            f"Economics: Income {income}/yr, Ration Card: {ration_card}, Housing: {housing_type}."
        )
        # SAVE FULL PROFILE FOR PDF
        st.session_state['full_profile_str'] = profile_string
        
        return profile_string
    
    return None