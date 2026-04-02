from env.environment import IncidentEnv
from env.agent import get_action

env = IncidentEnv()
obs = env.reset()

total_score = 0

while True:
    action = get_action(obs)
    obs, reward, done, _ = env.step(action)
    total_score += reward.score

    if done:
        break

print("Final Score:", total_score)
