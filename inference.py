import os
import sys
import time
import json
import requests
from openai import OpenAI

ENV_URL = "http://localhost:7860"

def solve_tasks():
    """
    Executes a series of incident response tasks.
    The agent dynamically reads environment observations, consults an LLM
    for the next logical action, and calculates a final performance score.
    """
    api_base = os.environ.get("API_BASE_URL", "http://localhost:8000") 
    api_key = os.environ.get("API_KEY", "dummy-key")
    client = OpenAI(base_url=api_base, api_key=api_key)
    
    tasks = [
        "suspicious_login_investigation",
        "malware_containment_protocol",
        "data_exfiltration_audit"
    ]
    
    time.sleep(2) 
    
    for task_name in tasks:
        print(f"[START] task={task_name}", flush=True)
        
        try:
            reset_response = requests.post(f"{ENV_URL}/reset", json={}).json()
            current_observation = reset_response.get("observation", "Start investigation.")
            
            total_reward = 0.0
            steps_taken = 0
            max_steps = 5
            
            for step in range(max_steps):
                steps_taken += 1
                
                try:
                    llm_response = client.chat.completions.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {
                                "role": "system", 
                                "content": "You are an elite cybersecurity AI. Analyze the observation and respond ONLY with a valid JSON object in this format: {\"command\": \"your_action_here\"}."
                            },
                            {
                                "role": "user", 
                                "content": f"Task: {task_name}. Observation: {current_observation}. What is your next command?"
                            }
                        ],
                        max_tokens=50
                    )
                    ai_text = llm_response.choices[0].message.content.strip()
                    
                    try:
                        if ai_text.startswith("```json"):
                            ai_text = ai_text[7:-3]
                        elif ai_text.startswith("```"):
                            ai_text = ai_text[3:-3]
                            
                        ai_chosen_action = json.loads(ai_text)
                    except json.JSONDecodeError:
                        ai_chosen_action = {"command": f"fallback_investigate_step_{step}"}
                        
                except Exception as llm_error:
                    ai_chosen_action = {"command": "system_fallback_action"}
                
                step_response = requests.post(
                    f"{ENV_URL}/step", 
                    json={"action": ai_chosen_action}
                ).json()
                
                current_observation = step_response.get("observation", "No observation provided.")
                reward = step_response.get("reward", 0.0)
                is_done = step_response.get("done", False)
                
                total_reward += reward
                
                print(f"[STEP] step={steps_taken} reward={reward}", flush=True)
                
                if is_done:
                    break
                    
            calculated_score = total_reward / steps_taken
            final_score = max(0.01, min(0.99, calculated_score)) 
            
            print(f"[END] task={task_name} score={final_score:.2f} steps={steps_taken}", flush=True)
            
        except Exception as e:
            print(f"Error communicating with environment: {e}", file=sys.stderr)
            print(f"[END] task={task_name} score=0.01 steps={steps_taken}", flush=True)

if __name__ == "__main__":
    solve_tasks()
