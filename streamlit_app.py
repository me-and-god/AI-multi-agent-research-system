import streamlit as st
from system.workflow import generate_report

st.title("AI Research Agent")

goal = st.text_area("Enter your goal")

if st.button("Generate Report"):
    with st.spinner("Thinking..."):
        result = generate_report(goal)

    st.subheader("Final Report")
    st.write(result)