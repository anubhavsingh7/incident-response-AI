from env.environment import IncidentEnv
from env.agent import get_action
from env.models import Action

def main():
    env = IncidentEnv()
    obs = env.reset()

    total_score = 0.0

    while True:
        action = get_action(obs)

        
        action_obj = Action(**action.model_dump())

        obs, reward, done, _ = env.step(action_obj)

        total_score += reward["score"]

        if done:
            break

    print(total_score)

if __name__ == "__main__":
    main()
