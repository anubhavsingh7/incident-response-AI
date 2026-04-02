from env.environment import IncidentEnv
from env.agent import get_action

def main():
    env = IncidentEnv()
    obs = env.reset()

    total_score = 0.0

    while True:
        action = get_action(obs)
        obs, reward, done, info = env.step(action)

        total_score += reward.score

        if done:
            break

    # 🔥 IMPORTANT: print ONLY final score number
    print(total_score)

if __name__ == "__main__":
    main()
