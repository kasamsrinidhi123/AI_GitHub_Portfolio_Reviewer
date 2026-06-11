import streamlit as st

def show_profile(profile):

    col1, col2 = st.columns([1, 3])

    with col1:

        if profile.get("avatar_url"):
            st.image(
                profile["avatar_url"],
                width=150
            )
        else:
            st.info("No profile image available")

    with col2:

        st.markdown(
            f"# {profile.get('name', profile.get('login', 'GitHub User'))}"
        )

        st.write(
            profile.get(
                "bio",
                "No bio available"
            )
        )

        st.write(
            f"👥 Followers: {profile.get('followers', 0)}"
        )

        st.write(
            f"📦 Repositories: {profile.get('public_repos', 0)}"
        )

        if profile.get("html_url"):
            st.link_button(
                "🔗 GitHub Profile",
                profile["html_url"]
            )