import streamlit as st

def show_projects(repos):

    st.markdown("# 🏆 Top Projects")
    st.text_input("🔍 Search Repository", key="repo_search")
    search = st.session_state.repo_search.lower()

    if search:
        repos = [
            repo
            for repo in repos
            if search in repo["name"].lower()
    ]

    repos = sorted(
        repos,
        key=lambda x: x["stargazers_count"],
        reverse=True
    )

    for repo in repos[:5]:

        with st.container():

            st.markdown(
                f"""
### ⭐ {repo['name']}

{repo.get('description','No description available')}
"""
            )

            st.link_button(
                "Open Repository",
                repo["html_url"]
            )

            st.divider()