def get_languages(repos):

    languages = {}

    for repo in repos:

        lang = repo["language"]

        if lang:

            languages[lang] = languages.get(lang, 0) + 1

    return languages

def get_strengths(repo_count, language_count, readme_count):

    strengths = []

    if repo_count >= 10:
        strengths.append("Good number of projects")

    if language_count >= 3:
        strengths.append("Good technology diversity")

    if readme_count >= repo_count * 0.7:
        strengths.append("Well documented repositories")

    if repo_count >= 15:
        strengths.append("Strong project portfolio")

    return strengths


def get_recommendations(repo_count, language_count, readme_count):

    recommendations = []

    if repo_count < 10:
        recommendations.append(
            "Add more projects to strengthen your portfolio."
        )

    if language_count < 3:
        recommendations.append(
            "Explore additional technologies and programming languages."
        )

    if readme_count < repo_count:
        recommendations.append(
            "Add README files to all repositories."
        )

    if repo_count < 15:
        recommendations.append(
            "Build more real-world projects with detailed documentation."
        )

    return recommendations