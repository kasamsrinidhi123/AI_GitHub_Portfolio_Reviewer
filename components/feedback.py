import streamlit as st

def show_feedback(
    strengths,
    recommendations
):

    st.markdown("### 🌟 Strengths")

    for item in strengths:
        st.success(item)

    st.markdown("### 📌 Recommendations")

    for item in recommendations:
        st.warning(item)