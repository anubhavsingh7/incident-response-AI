memory = []

def add_memory(obs, action, reward):
    memory.append({
        "logs": obs.logs,
        "alert": obs.alert,
        "action": {
            "issue_type": action.issue_type,
            "severity": action.severity,
            "resolution": action.resolution
        },
        "score": reward.score,
        "feedback": reward.feedback
    })

def get_recent_failures(n=3):
    failures = [m for m in memory if m["score"] < 0.7]
    return failures[-n:]