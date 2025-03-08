import streamlit as st
import requests

# Streamlit UI elements
st.title("AI-Powered Resume Analyzer")

resume_text = st.text_area("Paste your resume here:")

if st.button("Analyze"):
    if resume_text:
        # Send the resume text to the Flask backend for analysis
        response = requests.post("http://127.0.0.1:5000/analyze", json={"resume_text": resume_text})
        result = response.json()

        if "error" in result:
            st.error(result["error"])
        else:
            st.subheader("Analysis Results:")
            st.write(f"Entities found: {result['entities']}")
            st.write(f"Best Job Fit: {result['job_fit']} with score: {result['score']}")
    else:
        st.warning("Please enter your resume text before clicking 'Analyze'.")
