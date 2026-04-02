tasks = [
    {
        "logs": "Database connection timeout",
        "alert": "Latency spike",
        "expected": {"issue_type": "database", "severity": "high"}
    },
    {
        "logs": "CPU usage high",
        "alert": "Resource alert",
        "expected": {"issue_type": "cpu", "severity": "medium"}
    },
    {
        "logs": "Disk almost full",
        "alert": "Storage warning",
        "expected": {"issue_type": "disk", "severity": "high"}
    }
]
