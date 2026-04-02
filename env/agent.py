from env.models import Action

def get_action(observation):
    logs = observation.logs.lower()

    if "database" in logs:
        return Action("database", "high", "Restart DB")

    elif "cpu" in logs:
        return Action("cpu", "medium", "Optimize CPU")

    elif "disk" in logs:
        return Action("disk", "high", "Clean disk")

    elif "memory" in logs:
        return Action("memory", "high", "Fix memory leak")

    elif "login" in logs or "security" in logs:
        return Action("security", "high", "Block IP")

    return Action("unknown", "low", "Investigate")
