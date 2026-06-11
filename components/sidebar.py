import streamlit as st

def show_sidebar():

    st.sidebar.title("🚀 GitHub Reviewer")

    page = st.sidebar.radio(
        "Navigation",
        [
            "Dashboard",
            "Profile",
            "Analytics",
            "Top Projects"
            "Repository Analyzer",
            "AI Portfolio Assistant"

        ]
    )

    return page