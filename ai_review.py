import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key="YOUR GEMINI API")

def fallback_answer(user_prompt, repo_count, languages, score):
    question = user_prompt.lower()

    if "repository" in question:
        return f"This profile contains {repo_count} repositories."

    elif "language" in question:
        return f"The profile uses: {', '.join(languages.keys())}."

    elif "score" in question:
        return f"The portfolio score is {score}/100."

    elif "readme" in question:
        return f"This profile contains {repo_count} README files."

    else:
        return "Please ask about repositories, languages, README files, or portfolio score."

def generate_review(
    user_prompt,
    profile,
    repo_details,
    readme_text
):
    try:

        prompt = f"""
You are an expert GitHub Portfolio Reviewer.

========================
PROFILE INFORMATION
========================

Name:
{profile.get('name', 'N/A')}

Username:
{profile.get('login', 'N/A')}

Bio:
{profile.get('bio', 'No bio available')}

Followers:
{profile.get('followers', 0)}

Public Repositories:
{profile.get('public_repos', 0)}

========================
REPOSITORY INFORMATION
========================

{repo_details}

========================
README CONTENT
========================

{readme_text}

========================
USER QUESTION
========================

{user_prompt}

========================
INSTRUCTIONS
========================

Answer ONLY using the information provided above.

You can answer questions such as:

- Analyze this GitHub profile
- What skills does this developer have?
- Is this profile internship-ready?
- What are the strengths and weaknesses?
- What improvements do you recommend?
- Which project should be highlighted on a resume?
- Is this portfolio recruiter-friendly?
- Summarize this repository
- What does this repository do?
- What technologies are used?
- Explain this project in simple language
- Is this project resume-worthy?
- What problem does this project solve?
- Explain the architecture
- Generate interview questions based on this project
- Evaluate documentation quality
- Evaluate README quality

Rules:

- Use README content whenever available.
- Use repository details whenever available.
- Use profile information whenever available.
- If information is missing, clearly say so.
- Keep answers professional.
- Keep answers concise and easy to understand.
"""

        model = genai.GenerativeModel(
            "gemini-2.5-flash"
        )

        response = model.generate_content(
            prompt
        )

        if hasattr(response, "text"):
            return response.text

        return str(response)

    except Exception as e:
        return f"Error: {str(e)}"