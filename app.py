import streamlit as st
from src.agents import run_outreach_campaign

# Page Config
st.set_page_config(page_title="AI Outreach Manager", page_icon="🤖", layout="wide")

st.title("🤖 Multi-Agent Outreach Campaign Manager")
st.markdown("""
This system uses **CrewAI** to orchestrate three agents:
1. **Analyst Agent**: Reads customer data.
2. **Copywriter Agent**: Drafts highly personalized scripts and emails.
3. **Outreach Agent**: Executes the call via Twilio and sends the email.
""")

st.divider()

# Layout
col1, col2 = st.columns([1, 2])

with col1:
    st.header("👤 Customer Details")
    with st.form("customer_form"):
        name = st.text_input("Customer Name", "Jane Smith")
        company = st.text_input("Company", "Global Logistics Corp")
        industry = st.text_input("Industry", "Supply Chain")
        pain_points = st.text_area("Pain Points", "Delayed shipments, poor tracking visibility, high operational costs.")
        phone = st.text_input("Phone Number (Include Country Code)", "+12345678900")
        email = st.text_input("Email Address", "jane.smith@example.com")
        
        submit_btn = st.form_submit_button("Launch Campaign 🚀", type="primary", use_container_width=True)

with col2:
    st.header("📊 Campaign Output")
    
    if submit_btn:
        customer_data = {
            "name": name,
            "company": company,
            "industry": industry,
            "pain_points": pain_points,
            "phone": phone,
            "email": email
        }
        
        with st.spinner("Agents are analyzing, writing, and executing... (This may take a minute)"):
            try:
                # Trigger the CrewAI workflow
                final_result = run_outreach_campaign(customer_data)
                
                st.success("✅ Campaign Executed Successfully!")
                
                # Display the final output from the Outreach Manager agent
                st.markdown("### 📋 Final Execution Report")
                
                # CrewAI returns an object in recent versions, converting to string formats it properly
                st.write(str(final_result)) 
                
            except Exception as e:
                st.error(f"An error occurred during execution: {str(e)}")
    else:
        st.info("👈 Fill out the customer details and click 'Launch Campaign' to see the AI agents in action.")