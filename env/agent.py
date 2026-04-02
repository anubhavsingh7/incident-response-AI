from env.models import Action

def get_action(observation):
    logs = observation.logs.lower()


    if "database" in logs or "replication" in logs:
        return Action(
            issue_type="database",
            severity="high",
            resolution="Check database connections and restart DB service"
        )

    
    elif "cpu" in logs:
        return Action(
            issue_type="cpu",
            severity="medium",
            resolution="Optimize processes and reduce CPU load"
        )

