import streamlit as st
import plotly.express as px
import pandas as pd


def show_star_chart(repos):

    data = []

    for repo in repos:
        data.append({
            "Repository": repo["name"],
            "Stars": repo["stargazers_count"]
        })

    df = pd.DataFrame(data)

    if df["Stars"].sum() == 0:
        st.info("No starred repositories found yet.")
        return

    df = df.sort_values(
        by="Stars",
        ascending=False
    ).head(10)

    fig = px.bar(
        df,
        x="Repository",
        y="Stars",
        title="⭐ Top Repositories by Stars"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )