# Diploma for a judged category (score 1-100)
def diploma(score, max_score=100):
    percent = score * 100 / max_score
    if percent >= 75:
        return "gold"
    elif percent >= 50:
        return "silver"
    elif percent >= 25:
        return "bronze"
    return "participation"


for score in [82, 75, 51, 24]:
    print(score, "->", diploma(score))
