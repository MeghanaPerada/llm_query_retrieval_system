import streamlit as st
from chains import process_insurance_query  # your backend logic
from streamlit_extras.add_vertical_space import add_vertical_space

# --- Page Configuration ---
st.set_page_config(
    page_title="PolicyIQ: AI-Powered Insurance Query Engine",
    layout="wide",
)

# --- Custom Dark Styling ---
st.markdown("""
<style>
    html, body {
        background-color: #111827;
        color: #f9fafb;
        height: 100%;
        margin: 0;
        padding: 0;
    }
    .main {
        max-width: 1000px;
        margin: auto;
        padding: 2rem;
    }
    .stTextInput > div > div,
    .stFileUploader > div > div {
        background: #1f2937;
        color: #f9fafb;
        border-radius: 8px;
        padding: 10px;
    }
    .stButton>button {
        background-color: #10b981;
        color: white;
        border-radius: 8px;
        padding: 0.6em 1.2em;
    }
    .stButton>button:hover {
        background-color: #059669;
    }
    .highlight-box {
        background-color: #1e40af;
        padding: 1rem;
        border-radius: 12px;
        color: #f9fafb;
        font-weight: 500;
        margin-top: 10px;
    }
    .title-centered {
        text-align: center;
        font-size: 2.8em;
        font-weight: 700;
        color: #10b981;
        margin-bottom: 0.2em;
    }
    .subtitle-centered {
        text-align: center;
        font-size: 1.2em;
        color: #d1d5db;
        margin-bottom: 2em;
    }
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        font-size: 0.9rem;
        text-align: center;
        padding: 1rem;
        background-color: #111827;
        color: #9ca3af;
        z-index: 9999;
    }
</style>
""", unsafe_allow_html=True)

# --- Main Container ---
with st.container():
    st.markdown("<div class='main'>", unsafe_allow_html=True)

    # --- Header ---
    st.markdown("<div class='title-centered'>PolicyIQ: AI-Powered Insurance Query Engine</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle-centered'>Understand Your Insurance Coverage. Instantly.</div>", unsafe_allow_html=True)

    add_vertical_space(1)

    # --- Input Section ---
    st.subheader("1. Enter Your Query")
    query = st.text_input("Enter your natural language insurance query", placeholder="e.g. 46M, knee surgery in Pune, 3-month-old policy")

    add_vertical_space(1)

    st.subheader("2. Upload Policy Document")
    uploaded_file = st.file_uploader(
        "Upload PDF, DOCX or TXT format file",
        type=["pdf", "docx", "txt"]
    )

    add_vertical_space(2)
    st.markdown("---")

    # --- Run Button ---
    if st.button("Run Decision Engine"):
        if not query.strip():
            st.warning("Please enter a valid query.")
        elif not uploaded_file:
            st.warning("Please upload a policy document.")
        else:
            with st.spinner("Processing your query..."):
                result = process_insurance_query(query, uploaded_file)

            st.success("✅ Decision complete")

            add_vertical_space(1)
            st.subheader("📋 Final Decision")
            st.markdown(f"<div class='highlight-box'>{result['decision']}</div>", unsafe_allow_html=True)

            add_vertical_space(1)
            st.subheader("🔎 Justification")
            for clause in result["justification_clauses"]:
                st.info(clause)

            add_vertical_space(1)
            st.subheader("📊 Confidence Score")
            st.progress(min(result["confidence"], 1.0))

            add_vertical_space(1)
            st.subheader("🧬 Extracted Entities")
            st.json(result["entities"])

    st.markdown("</div>", unsafe_allow_html=True)  # Close main container

# --- Footer ---
st.markdown("<div class='footer'>Built by Meghana & Shreethan — Powered by LLMs</div>", unsafe_allow_html=True)