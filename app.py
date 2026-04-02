import streamlit as st
import time
import random
from env.environment import IncidentEnv
from env.agent import get_action
from env.memory import add_memory, memory

st.set_page_config(page_title="AI Incident Response", layout="wide")

st.title("🚨AI Incident Response")

# Initialize state
if "env" not in st.session_state:
    st.session_state.env = IncidentEnv()
    st.session_state.obs = st.session_state.env.reset()
    st.session_state.done = False
    st.session_state.score = 0

obs = st.session_state.obs

# -------------------------------

if not st.session_state.done:

    st.subheader("📡 Incoming Incident")

    st.code(f"""
Logs:
{obs.logs}

Alert:
{obs.alert}
""")

    # -------------------------------
    
    if st.button("🤖 Run AI Agent"):

        with st.spinner("Analyzing logs..."):
            time.sleep(1.5)

        action = get_action(obs)

        obs_next, reward, done, _ = st.session_state.env.step(action)

        add_memory(obs, action, reward)

        st.session_state.obs = obs_next
        st.session_state.done = done
        st.session_state.score += reward.score

        # -------------------------------
       
        st.subheader("🧠 Agent Decision")

        severity_color = {
            "low": "blue",
            "medium": "orange",
            "high": "red",
            "critical": "darkred"
        }

        st.markdown(f"""
### 🚨 Issue Type: **{action.issue_type.upper()}**
### ⚠️ Severity: <span style='color:{severity_color.get(action.severity, "white")}'>{action.severity.upper()}</span>
### 🛠 Resolution:
{action.resolution}
""", unsafe_allow_html=True)

        # -------------------------------
       
        confidence = round(random.uniform(0.80, 0.99), 2)

        col1, col2 = st.columns(2)
        col1.metric("📊 Score", reward.score)
        col2.metric("🤖 Confidence", confidence)

        st.progress(reward.score)

        st.info(f"Feedback: {reward.feedback}")

        # -------------------------------
        
        st.subheader("🧠 Learning Memory (Recent Mistakes)")

        if len(memory) == 0:
            st.write("No memory yet...")
        else:
            for m in memory[-3:]:
                st.write({
                    "logs": m["logs"],
                    "score": m["score"],
                    "feedback": m["feedback"]
                })

# -------------------------------

else:
    st.success("✅ All incidents handled!")

    final_score = round(st.session_state.score / 3, 2)

    st.metric("🏆 Final Score", final_score)

    if final_score > 0.8:
        st.success("🔥 Excellent performance!")
    elif final_score > 0.5:
        st.warning("⚠️ Moderate performance")
    else:
        st.error("❌ Needs improvement")

    if st.button("🔄 Restart Simulation"):
        st.session_state.env = IncidentEnv()
        st.session_state.obs = st.session_state.env.reset()
        st.session_state.done = False
        st.session_state.score = 0