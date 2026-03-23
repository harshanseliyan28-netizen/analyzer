def calculate_score(issues):
    score = 100 - (issues * 2)
    return max(score, 0)