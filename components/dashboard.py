import streamlit as st

from components.dashboard_cards import show_cards
from components.language_chart import show_language_chart


def show_dashboard():

    st.header("🏠 Dashboard")

    # Dashboard Cards
    show_cards(
        st.session_state.repo_count,
        len(st.session_state.languages),
        st.session_state.readme_count,
        st.session_state.score
    )

    # Portfolio Grade
    st.success(
        f"🏅 Portfolio Grade: {st.session_state.grade}"
    )

    # Portfolio Level
    if st.session_state.score >= 90:
        level = "Expert"
    elif st.session_state.score >= 70:
        level = "Intermediate"
    else:
        level = "Beginner"

    st.info(
        f"🚀 Portfolio Level: {level}"
    )

    st.divider()

    

    # Proof of Concept Results
    st.header("🎯 Proof of Concept Results")

    st.info(f"""
Input:
GitHub Username = {st.session_state.profile['login']}

Output:
✅ Repositories Analyzed: {st.session_state.repo_count}
✅ Technologies Identified: {len(st.session_state.languages)}
✅ Portfolio Score: {st.session_state.score}
✅ Portfolio Grade: {st.session_state.grade}
✅ Recommendations Generated Automatically
""")
# User Prompt


if "user_prompt" in st.session_state:
    st.code(st.session_state.user_prompt)

    st.divider()

    # Download Report
    report = f"""
GitHub Portfolio Report

Username: {st.session_state.profile['login']}
Repositories: {st.session_state.repo_count}
Languages: {len(st.session_state.languages)}
READMEs: {st.session_state.readme_count}
Score: {st.session_state.score}
Grade: {st.session_state.grade}

Strengths:
{chr(10).join(st.session_state.strengths)}

Recommendations:
{chr(10).join(st.session_state.recommendations)}
"""

    st.download_button(
        label="📄 Download Report",
        data=report,
        file_name="portfolio_report.txt",
        mime="text/plain"
    )

    st.divider()

    # Language Chart
    st.subheader("📊 Language Distribution")

    show_language_chart(
        st.session_state.languages
    )

    st.divider()

    # AI Summary
    st.subheader("🧐 AI Portfolio Summary")

    st.info(
        f"""
This GitHub portfolio contains {st.session_state.repo_count} repositories
and uses {len(st.session_state.languages)} technologies.

Strengths:
• {' • '.join(st.session_state.strengths)}

Areas for Improvement:
• {' • '.join(st.session_state.recommendations)}
"""
    )

st.divider()


if "ai_feedback" in st.session_state:
    st.write(st.session_state.ai_feedback)