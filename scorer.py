def calculate_score(repo_count, language_count, readme_count):

    score = 0

    score += min(repo_count * 3, 50)

    score += min(language_count * 10, 20)

    if repo_count > 0:
        score += (readme_count / repo_count) * 20

    score += 10

    return round(min(score, 100))