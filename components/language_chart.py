import streamlit as st
import plotly.express as px


def show_language_chart(languages):

    if not languages:
        return

    fig = px.pie(
        names=list(languages.keys()),
        values=list(languages.values()),
        title="🚀 Language Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)