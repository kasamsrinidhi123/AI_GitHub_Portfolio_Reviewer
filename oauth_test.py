import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("GITHUB_CLIENT_ID")
CLIENT_SECRET = os.getenv("GITHUB_CLIENT_SECRET")

st.title("GitHub OAuth Test")

# If no code exists, show login button
if "code" not in st.query_params:

    login_url = (
        f"https://github.com/login/oauth/authorize"
        f"?client_id={CLIENT_ID}"
        f"&scope=repo"
    )

    st.markdown(f"[🔐 Login with GitHub]({login_url})")

else:

    code = st.query_params["code"]

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

    # Handle expired/used code
    if "access_token" not in data:
        st.error("OAuth code expired or already used.")
        st.info("Please go back and login again.")
        st.write(data)
        st.stop()

    token = data["access_token"]
    st.session_state["github_token"] = token
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json"
    }

    repos = requests.get(
        "https://api.github.com/user/repos?visibility=all&per_page=100",
        headers=headers
    ).json()

    st.success("✅ Login Successful!")

    st.write(f"### Total Repositories Found: {len(repos)}")

    private_count = 0
    public_count = 0

    for repo in repos:

        if repo["private"]:
            private_count += 1
            st.write(f"🔒 {repo['name']} (Private)")
        else:
            public_count += 1
            st.write(f"🌐 {repo['name']} (Public)")

    st.divider()

    st.success(f"🌐 Public Repositories: {public_count}")
    st.success(f"🔒 Private Repositories: {private_count}")