from env.environment import IncidentEnv
from env.agent import get_action

def run_inference():
    env = IncidentEnv()
    obs = env.reset()
    total_score = 0

    while True:
        action = get_action(obs)
        obs, reward, done, _ = env.step(action)
        total_score += reward.score

        if done:
            break

    return {"score": total_score}

if __name__ == "__main__":
    print(run_inference())
