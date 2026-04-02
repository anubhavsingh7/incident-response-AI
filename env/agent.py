from env.models import Action
from env.memory import get_recent_failures


def get_action(obs):
    log = obs.logs.lower()

    # -------------------------------

    failures = get_recent_failures()

    for f in failures:
        if f["logs"].lower() in log:
            return Action(
                issue_type=f["action"]["issue_type"],
                severity=f["action"]["severity"],
                resolution="Adjusted strategy based on past failure."
            )


    # DATABASE ISSUES

    if "database" in log or "timeout" in log:
        return Action(
            issue_type="database",
            severity="high",
            resolution="Check database connections, restart DB service, and monitor query performance."
        )

    # SERVER ISSUES

    elif "503" in log or "unavailable" in log or "crash" in log:
        return Action(
            issue_type="server",
            severity="critical",
            resolution="Restart server instances and investigate application logs for failures."
        )

    # NETWORK ISSUES

    elif "network" in log or "packet loss" in log or "dns" in log:
        return Action(
            issue_type="network",
            severity="high",
            resolution="Check network routes, DNS configuration, and reduce packet loss."
        )

    # DISK / SYSTEM ISSUES

    elif "disk" in log or "storage" in log:
        return Action(
            issue_type="server",
            severity="high",
            resolution="Free up disk space and optimize storage usage."
        )

    # FALLBACK
    else:
        return Action(
            issue_type="unknown",
            severity="medium",
            resolution="Analyze logs further and escalate if needed."
        )