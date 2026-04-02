TASKS = [
    {
        "id": "easy",
        "logs": "Error: Database connection timeout at 10:32PM",
        "alert": "Service latency spike",
        "expected": {
            "issue_type": "database",
            "severity": "high"
        }
    },
    {
        "id": "medium",
        "logs": "503 errors across multiple endpoints",
        "alert": "API unavailable",
        "expected": {
            "issue_type": "server",
            "severity": "critical"
        }
    },
    {
        "id": "hard",
        "logs": "Intermittent packet loss detected, high retry rate",
        "alert": "Slow response in multiple regions",
        "expected": {
            "issue_type": "network",
            "severity": "high"
        }
    },
    {
    "id": "extra1",
    "logs": "Disk space full error",
    "alert": "System failure",
    "expected": {
        "issue_type": "server",
        "severity": "high"
    }
},
{
    "id": "extra2",
    "logs": "DNS resolution failed",
    "alert": "Service unreachable",
    "expected": {
        "issue_type": "network",
        "severity": "critical"
    }
}
]