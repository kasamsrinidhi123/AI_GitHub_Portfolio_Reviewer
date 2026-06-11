import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("GITHUB_CLIENT_ID")
CLIENT_SECRET = os.getenv("GITHUB_CLIENT_SECRET")

from github_api import (
    get_repositories,
    get_user_profile,
    count_readmes,
    get_private_repositories,
    count_public_private,
    get_authenticated_user,
    get_readme
)

from analyzer import (
    get_languages,
    get_strengths,
    get_recommendations
)
from github_api import get_readme
from ai_review import generate_review, fallback_answer
from scorer import calculate_score
from components.star_chart import show_star_chart
from components.dashboard import show_dashboard
from components.profile_card import show_profile
from components.dashboard_cards import show_cards
from components.feedback import show_feedback
from components.projects import show_projects
from components.language_chart import show_language_chart
from components.repository_analyzer import show_repository_analyzer

token = st.session_state.get("github_token")
logged_in_username = None

if token:
    user_data = get_authenticated_user(token)

    if user_data:
        logged_in_username = user_data["login"]
# ------------------------------
# PAGE CONFIG
# ------------------------------

st.set_page_config(
    page_title="AI GitHub Portfolio Reviewer",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ------------------------------
# CSS
# ------------------------------

with open("style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# ------------------------------
# SESSION STATE
# ------------------------------

if "page" not in st.session_state:
    st.session_state.page = "Dashboard"
# ------------------------------
# GITHUB OAUTH
# ------------------------------

params = st.query_params

if "code" in params and "github_token" not in st.session_state:

    code = params["code"]

    response = requests.post(
        "https://github.com/login/oauth/access_token",
        headers={"Accept": "application/json"},
        data={
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "code": code
        }
    )

    data = response.json()

    if "access_token" in data:
        st.session_state["github_token"] = data["access_token"]

if "github_token" not in st.session_state:

    login_url = (
        f"https://github.com/login/oauth/authorize"
        f"?client_id={CLIENT_ID}"
        f"&scope=repo"
    )

    st.sidebar.markdown(
        f"[🔐 Login with GitHub]({login_url})"
    )

else:

    st.sidebar.success("✅ GitHub Connected")
# ------------------------------
# SIDEBAR
# ------------------------------

st.sidebar.title("🚀 GitHub Reviewer")

if st.sidebar.button("🏠 Dashboard"):
    st.session_state.page = "Dashboard"

if st.sidebar.button("👤 Profile"):
    st.session_state.page = "Profile"

if st.sidebar.button("📊 Analytics"):
    st.session_state.page = "Analytics"

if st.sidebar.button("🏆 Top Projects"):
    st.session_state.page = "Projects"

if st.sidebar.button("🔍 Repository Analyzer"):
    st.session_state.page = "Repository Analyzer"

if st.sidebar.button("📝 AI Portfolio Assistant"):
    st.session_state.page = "AI Portfolio Assistant"

page = st.session_state.page

# ------------------------------
# HEADER
# ------------------------------

st.title("🚀 AI GitHub Portfolio Reviewer")

st.write(
    "Analyze GitHub portfolios and get recruiter-style feedback."
)

# ------------------------------
# USERNAME
# ------------------------------
username = st.text_input(
    "Enter GitHub Username",
    key="username"
)

# ------------------------------
# ANALYZE
# ------------------------------

if st.button("🚀 Analyze Portfolio",key="analyze2"):
    
    token = st.session_state.get("github_token")
    if token and username.lower() == logged_in_username.lower():

        repos = get_private_repositories(token)

        profile = get_user_profile(username)

    else:

        repos = get_repositories(username)

        profile = get_user_profile(username)
        st.session_state.repos = repos
        st.session_state.profile = profile
    if token and username.lower() != logged_in_username.lower():

        st.info(
            f"Analyzing public profile of {username}. "
            f"Private repositories are available only for {logged_in_username}."
        )

    if repos is None or profile is None:
        st.error("GitHub user not found")
        st.stop()

    languages = get_languages(repos)
    st.session_state.languages = languages

    repo_count = len(repos)
    public_repos = len(
        [repo for repo in repos if not repo["private"]]
    )

    private_repos = len(
        [repo for repo in repos if repo["private"]]
    )

    st.success(f"🌐 Public Repositories: {public_repos}")
    st.success(f"🔒 Private Repositories: {private_repos}")

    readme_count = repo_count

    score = calculate_score(
        repo_count,
        len(languages),
        readme_count
    )
    

    if score >= 90:
       grade = "A+"
    elif score >= 80:
       grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    else:
        grade = "D"

    strengths = get_strengths(
        repo_count,
        len(languages),
        readme_count
    )

    recommendations = get_recommendations(
        repo_count,
        len(languages),
        readme_count
    )

    st.session_state.grade = grade

    st.session_state.profile = profile
    st.session_state.repos = repos
    st.session_state.public_repos = public_repos
    st.session_state.private_repos = private_repos
    st.session_state.languages = languages
    st.session_state.repo_count = repo_count
    st.session_state.readme_count = readme_count
    st.session_state.score = score
    st.session_state.strengths = strengths
    st.session_state.recommendations = recommendations

# ------------------------------
# DASHBOARD
# ------------------------------
if page == "Dashboard":

    if "profile" not in st.session_state:
        st.info("👆 Enter a GitHub username and click Analyze Portfolio.")
    else:
        show_dashboard()

# ------------------------------
# PROFILE
# ------------------------------

elif page == "Profile":

    st.header("👤 GitHub Profile")

    show_profile(
        st.session_state.profile
    )
# ANALYTICS

elif page == "Analytics":

    if "profile" not in st.session_state:
        st.info("Analyze a GitHub profile first.")
    else:
        st.header("📊 Analytics")

        st.metric("Total Repositories", st.session_state.repo_count)
        st.metric("Public Repositories", st.session_state.public_repos)
        st.metric("Private Repositories", st.session_state.private_repos)
        st.metric("Languages", len(st.session_state.languages))
        st.metric("Score", st.session_state.score)

        show_language_chart(
            st.session_state.languages
        )

# ------------------------------
# PROJECTS
# ------------------------------

elif page == "Projects":

    show_projects(
        st.session_state.repos
    )

elif page == "Repository Analyzer":

    show_repository_analyzer(
        st.session_state.repos,
        username,
        st.session_state.get("github_token")
    )

elif page == "AI Portfolio Assistant":

    st.header("📝AI Portfolio Assistant")
    repos = st.session_state.get("repos", [])
    
    profile = st.session_state.get("profile")

    repo_details = ""

    for repo in repos:

        repo_details += f"""
    Repository: {repo['name']}
    Description: {repo.get('description', 'No description')}
    Language: {repo.get('language', 'Unknown')}
    Stars: {repo.get('stargazers_count', 0)}
    Forks: {repo.get('forks_count', 0)}
    URL: {repo.get('html_url', '')}

    """
    
    question = st.text_input(
        "Ask about this GitHub profile"
    )

    if st.button("Ask Gemini"):

        answer = generate_review(

            question,
            profile,
            repo_details,
            ""

        )
    
        if answer is None:
            answer = fallback_answer(
                question,
                st.session_state.repo_count,
                st.session_state.languages,
                st.session_state.score
            )
        st.session_state.user_prompt = question
        st.session_state.ai_feedback = answer

    if "user_prompt" in st.session_state:
        st.subheader("Question")
        st.write(st.session_state.user_prompt)

    if "ai_feedback" in st.session_state:
        st.subheader("Answer")
        st.success(st.session_state.ai_feedback)
# FOOTER
# ------------------------------

st.divider()

st.caption(
    "Built with ❤️ using Streamlit and GitHub API"
)