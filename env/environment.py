from env.models import Observation, Reward
from env.tasks import TASKS
from env.graders import grade

class IncidentEnv:
    def __init__(self):
        self.index = 0
        self.done = False

    def reset(self):
        self.index = 0
        self.done = False
        return self._get_obs()

    def _get_obs(self):
        task = TASKS[self.index]
        return Observation(
            incident_id=self.index,
            logs=task["logs"],
            alert=task["alert"]
        )

    def step(self, action):
        task = TASKS[self.index]
        score, feedback = grade(action, task["expected"])

        reward = Reward(score=score, feedback=feedback)

        self.index += 1
        if self.index >= len(TASKS):
            self.done = True

        obs = None if self.done else self._get_obs()
        return obs, reward, self.done, {}

    def state(self):
        return {"index": self.index, "done": self.done}