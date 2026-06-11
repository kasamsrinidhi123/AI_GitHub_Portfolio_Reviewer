import streamlit as st
from ai_review import generate_review
from github_api import get_readme


def show_repository_analyzer(
    repos,
    username=None,
    token=None
):

    profile = st.session_state.get("profile")

    st.header("🔍 Repository Analyzer")

    if not repos:
        st.warning("No repositories found.")
        return

    repo_names = [
        repo["name"]
        for repo in repos
    ]

    selected_repo = st.selectbox(
        "Select Repository",
        repo_names
    )

    repo = next(
        r for r in repos
        if r["name"] == selected_repo
    )

    st.divider()

    # Repository Details

    st.subheader(
        f"📁 {repo['name']}"
    )

    st.write(
        repo.get(
            "description",
            "No description available."
        )
    )

    st.write(
        f"💻 Language: {repo.get('language', 'Not Specified')}"
    )

    st.write(
        f"🔗 Repository URL: {repo['html_url']}"
    )

    st.divider()

    # Metrics

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "⭐ Stars",
            repo["stargazers_count"]
        )

    with col2:
        st.metric(
            "🍴 Forks",
            repo["forks_count"]
        )

    with col3:
        st.metric(
            "👀 Watchers",
            repo["watchers_count"]
        )

    st.divider()

    # Repository Score

    score = 50

    if repo.get("description"):
        score += 15

    if repo["stargazers_count"] > 0:
        score += 15

    if repo["forks_count"] > 0:
        score += 10

    if repo.get("language"):
        score += 10

    score = min(score, 100)

    st.success(
        f"🏆 Repository Score: {score}/100"
    )

    st.divider()

    # README

    readme = ""

    if username:

        try:
            readme = get_readme(
                username,
                selected_repo,
                token
            )

        except:
            readme = "README not available."

    # Repository AI Chat

    st.subheader(
        "💬 Ask About This Repository"
    )

    repo_question = st.text_input(
        "Ask anything about this repository",
        key="repo_question"
    )

    if st.button(
        "Ask Repository AI",
        key="repo_ai"
    ):

        repo_details = f"""
Repository Name:
{repo['name']}

Description:
{repo.get('description', 'No description')}

Language:
{repo.get('language', 'Unknown')}

Stars:
{repo['stargazers_count']}

Forks:
{repo['forks_count']}

Watchers:
{repo['watchers_count']}
"""

        answer = generate_review(
            repo_question,
            profile,
            repo_details,
            readme
        )

        st.subheader("Answer")

        st.success(answer)

    st.divider()

    # Repository Review

    st.subheader(
        "🤖 Repository Review"
    )

    strengths = []
    recommendations = []

    if repo.get("description"):
        strengths.append(
            "Repository has a description."
        )
    else:
        recommendations.append(
            "Add a clear repository description."
        )

    if repo.get("language"):
        strengths.append(
            f"Uses {repo['language']}."
        )

    if repo["stargazers_count"] > 0:
        strengths.append(
            "Repository has community interest."
        )
    else:
        recommendations.append(
            "Promote the project to gain visibility."
        )

    if repo["forks_count"] > 0:
        strengths.append(
            "Repository has forks."
        )
    else:
        recommendations.append(
            "Encourage collaboration and contributions."
        )

    st.markdown("### ✅ Strengths")

    if strengths:
        for item in strengths:
            st.success(item)
    else:
        st.warning(
            "No strengths identified."
        )

    st.markdown("### 📌 Recommendations")

    if recommendations:
        for item in recommendations:
            st.warning(item)
    else:
        st.success(
            "Repository looks strong."
        )

    st.divider()

    st.caption(
        "Repository-level analysis powered by GitHub + Gemini AI."
    )