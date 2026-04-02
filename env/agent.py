from env.models import Action

def get_action(observation):
    logs = observation.logs.lower()

    if "database" in logs:
        return Action(
            issue_type="database",
            severity="high",
            resolution="Restart DB"
        )

    elif "cpu" in logs:
        return Action(
            issue_type="cpu",
            severity="medium",
            resolution="Optimize CPU"
        )

    elif "disk" in logs:
        return Action(
            issue_type="disk",
            severity="high",
            resolution="Clean disk"
        )

    elif "memory" in logs:
        return Action(
            issue_type="memory",
            severity="high",
            resolution="Fix memory leak"
        )

    elif "login" in logs or "security" in logs:
        return Action(
            issue_type="security",
            severity="high",
            resolution="Block IP"
        )

    return Action(
        issue_type="unknown",
        severity="low",
        resolution="Investigate"
    )
