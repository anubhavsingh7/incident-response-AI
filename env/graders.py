def grade(action, expected):
    score = 0.0
    feedback = []

    if action.issue_type == expected["issue_type"]:
        score += 0.4
    else:
        feedback.append("Wrong issue type")

    if action.severity == expected["severity"]:
        score += 0.3
    else:
        feedback.append("Incorrect severity")

    if len(action.resolution) > 30:
        score += 0.3
    else:
        feedback.append("Weak resolution")

    if action.issue_type == "unknown":
        score -= 0.2    

    return score, ", ".join(feedback)