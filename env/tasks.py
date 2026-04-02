tasks = [


    {
        "logs": "Database connection timeout error",
        "alert": "Latency spike",
        "expected": {
            "issue_type": "database",
            "severity": "high"
        }
    },
    {
        "logs": "CPU usage high on server",
        "alert": "Resource usage alert",
        "expected": {
            "issue_type": "cpu",
            "severity": "medium"
        }
    },

    
    {
        "logs": "Disk almost full, storage at 95%",
        "alert": "Storage warning",
        "expected": {
            "issue_type": "disk",
            "severity": "high"
        }
    },
    {
        "logs": "API response time increasing gradually",
        "alert": "Performance degradation",
        "expected": {
            "issue_type": "network",
            "severity": "medium"
        }
    },
    {
        "logs": "Memory leak detected in application",
        "alert": "Memory usage alert",
        "expected": {
            "issue_type": "memory",
            "severity": "high"
        }
    },


    {
        "logs": "Multiple failed login attempts detected from unknown IP",
        "alert": "Security breach attempt",
        "expected": {
            "issue_type": "security",
            "severity": "high"
        }
    },
    {
        "logs": "Service unavailable intermittently, possible load balancer issue",
        "alert": "Service disruption",
        "expected": {
            "issue_type": "network",
            "severity": "high"
        }
    },
    {
        "logs": "Database replication lag detected across nodes",
        "alert": "Data inconsistency risk",
        "expected": {
            "issue_type": "database",
            "severity": "medium"
        }
    }
]
