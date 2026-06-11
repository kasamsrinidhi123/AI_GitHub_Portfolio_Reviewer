import streamlit as st

def show_cards(
    repo_count,
    language_count,
    readme_count,
    score
):

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("📦 Repositories", repo_count)
    c2.metric("💻 Languages", language_count)
    c3.metric("📄 READMEs", readme_count)
    c4.metric("⭐ Score", score)