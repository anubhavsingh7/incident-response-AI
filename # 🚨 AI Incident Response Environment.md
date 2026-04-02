# 🚨 AI Incident Response Environment

# 🧠 Overview

This project simulates real-world DevOps incident handling using AI agents.

The agent:
- Reads system logs
- Identifies issue type
- Assigns severity
- Suggests resolution

It also improves over time using feedback from previous mistakes.

---

# 🎯 Features

- Real-world incident simulation
- Agent-based decision making
- Reward-based evaluation (0.0–1.0)
- Self-learning via memory
- Interactive UI using Streamlit

---

# 📊 Tasks

1. Database timeout (easy)
2. API outage (medium)
3. Network issue (hard)

---

# ⚙️ Action Space

- issue_type: database | network | server | unknown
- severity: low | medium | high | critical
- resolution: text

---

# 📥 Observation Space

- logs
- alert

---

# 🎯 Reward System

- Issue type: 0.4
- Severity: 0.3
- Resolution: 0.3

---

# 🚀 Setup

```bash
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt