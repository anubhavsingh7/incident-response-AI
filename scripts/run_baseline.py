from env.environment import IncidentEnv
from env.agent import get_action
from env.memory import add_memory


def run():
    env = IncidentEnv()
    obs = env.reset()
    total_score = 0
    step = 1

    print("\n🚨 Starting Incident Response Simulation...\n")

    while True:
        print(f"\n--- Step {step} ---")

        print("\n Incoming Incident:")
        print("Logs:", obs.logs)
        print("Alert:", obs.alert)

       
        action = get_action(obs)

        print("\n Agent Decision:")
        print("Issue Type:", action.issue_type)
        print("Severity:", action.severity)
        print("Resolution:", action.resolution)

        obs_next, reward, done, _ = env.step(action)

        print("\n📊 Evaluation:")
        print("Score:", reward.score)
        print("Feedback:", reward.feedback)

        add_memory(obs, action, reward)

        total_score += reward.score
        obs = obs_next
        step += 1

        if done:
            break

    final_score = total_score / 3
    print("\n✅ Simulation Complete")
    print(" Final Score:", round(final_score, 2))


if __name__ == "__main__":
    run()