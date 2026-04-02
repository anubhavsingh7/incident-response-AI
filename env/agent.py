from env.models import Action

def get_action(obs):
    logs = obs.logs.lower()

    if "database" in logs:
        return Action(issue_type="database", severity="high", resolution="Restart DB")

    elif "cpu" in logs:
        return Action(issue_type="cpu", severity="medium", resolution="Optimize CPU")

    elif "disk" in logs:
        return Action(issue_type="disk", severity="high", resolution="Clean disk")

    return Action(issue_type="unknown", severity="low", resolution="Investigate")
