from env.models import Observation, Reward
from env.tasks import tasks

class IncidentEnv:
    def __init__(self):
        self.tasks = tasks
        self.index = 0

    def reset(self):
        self.index = 0
        task = self.tasks[self.index]

        return Observation(
            incident_id=self.index,
            logs=task["logs"],
            alert=task["alert"]
        )

    def step(self, action):
        task = self.tasks[self.index]
        score = 0.0

        if action.issue_type == task["expected"]["issue_type"]:
            score += 0.5

        if action.severity == task["expected"]["severity"]:
            score += 0.5

        self.index += 1
        done = self.index >= len(self.tasks)

        if not done:
            next_task = self.tasks[self.index]
            obs = Observation(
                incident_id=self.index,
                logs=next_task["logs"],
                alert=next_task["alert"]
            )
        else:
            obs = Observation(
                incident_id=self.index,
                logs="completed",
                alert="done"
            )

        return obs, Reward(score=score), done, {}
