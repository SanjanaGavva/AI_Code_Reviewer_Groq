import streamlit as st
from code_reviewer import review_code

st.set_page_config(page_title="AI Code Reviewer",page_icon="💻",layout="wide")
                   
st.title("💻 AI Code Reviwer using Grok API")

code=st.text_area("Paste your code here",height=400)

if st.button("Review Code"):
    if not code.strip():
        st.warning("Please paste some code.")
    else:
        with st.spinner("Reviewing ..."):
            result=review_code(code)
        st.markdown(result)