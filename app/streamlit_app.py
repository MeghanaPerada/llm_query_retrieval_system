import streamlit as st
from app.chains import process_insurance_query

st.title("📄 LLM Query-Retrieval System")
query = st.text_input("Enter Insurance Query", placeholder="e.g. 46M, knee surgery in Pune, 3-month policy")

if st.button("Submit"):
    with st.spinner("Processing..."):
        result = process_insurance_query(query)
        st.success("✅ Decision Made")
        st.json(result)