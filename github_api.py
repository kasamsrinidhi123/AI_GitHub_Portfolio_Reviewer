import streamlit as st
import requests
import base64

BASE_URL = "https://api.github.com"


@st.cache_data(ttl=600)
def get_user_profile(username):

    url = f"{BASE_URL}/users/{username}"

    response = requests.get(url)

    print("PROFILE STATUS:", response.status_code)

    if response.status_code != 200:
        return None

    return response.json()


@st.cache_data(ttl=600)
def get_repositories(username):

    url = f"{BASE_URL}/users/{username}/repos?per_page=100"

    response = requests.get(url)

    print("REPO STATUS:", response.status_code)

    if response.status_code != 200:
        return None

    return response.json()


@st.cache_data(ttl=600)
def get_private_repositories(token):

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json"
    }

    response = requests.get(
        f"{BASE_URL}/user/repos?visibility=all&per_page=100",
        headers=headers
    )

    print("PRIVATE REPO STATUS:", response.status_code)

    if response.status_code != 200:
        return None

    return response.json()


@st.cache_data(ttl=600)
def count_readmes(username, repos):

    count = 0

    for repo in repos:

        repo_name = repo["name"]

        url = (
            f"{BASE_URL}/repos/"
            f"{username}/{repo_name}/readme"
        )

        response = requests.get(url)

        if response.status_code == 200:
            count += 1

    return count


def count_public_private(repos):

    public_count = len(
        [repo for repo in repos if not repo["private"]]
    )

    private_count = len(
        [repo for repo in repos if repo["private"]]
    )

    return public_count, private_count
def get_authenticated_user(token):

    headers = {
        "Authorization": f"token {token}"
    }

    response = requests.get(
        "https://api.github.com/user",
        headers=headers
    )

    if response.status_code == 200:
        return response.json()

    return None

def get_readme(username, repo_name, token=None):

    url = f"https://api.github.com/repos/{username}/{repo_name}/readme"

    headers = {}

    if token:
        headers["Authorization"] = f"token {token}"

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return "README not found."

    data = response.json()

    content = base64.b64decode(
        data["content"]
    ).decode("utf-8")

    return content
import base64

def get_readme(username, repo_name, token=None):

    headers = {}

    if token:
        headers["Authorization"] = f"token {token}"

    url = f"https://api.github.com/repos/{username}/{repo_name}/readme"

    response = requests.get(url, headers=headers)

    if response.status_code == 200:

        data = response.json()

        return base64.b64decode(
            data["content"]
        ).decode("utf-8")

    return "README not available."