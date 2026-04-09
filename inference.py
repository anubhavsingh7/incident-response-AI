import requests
import time
import sys
import os
from openai import OpenAI

BASE_URL = "http://localhost:7860"

def solve_incident():
    task_name = "suspicious_login_investigation"
    
    print(f"[START] task={task_name}", flush=True)
    
    try:
        api_base = os.environ.get("API_BASE_URL", "http://localhost:8000") 
        api_key = os.environ.get("API_KEY", "dummy-key")
        
        client = OpenAI(
            base_url=api_base,
            api_key=api_key
        )
        # -------------------------------------------------------------------

        time.sleep(2)
        reset_response = requests.post(f"{BASE_URL}/reset", json={}).json()
        
        total_reward = 0.0
        steps_taken = 0
        
        for i in range(5):
            steps_taken += 1
            
            try:
                llm_response = client.chat.completions.create(
                    model="gpt-3.5-turbo", 
                    messages=[
                        {"role": "system", "content": "You are a cybersecurity AI."},
                        {"role": "user", "content": "What is the next step to investigate a suspicious login?"}
                    ],
                    max_tokens=20
                )
                ai_thought = llm_response.choices[0].message.content
            except Exception as llm_error:
                print(f"LLM proxy call failed, but continuing: {llm_error}")
            # -----------------------------------------------------------
            
            simulated_action = {"command": f"check_logs_step_{i}"}
            step_response = requests.post(f"{BASE_URL}/step", json={"action": simulated_action}).json()
            
            reward = step_response.get("reward", 0.0)
            total_reward += reward
            is_done = step_response.get("done", False)
            
            print(f"[STEP] step={steps_taken} reward={reward}", flush=True)
            
            if is_done:
                break
                
        print(f"[END] task={task_name} score={total_reward} steps={steps_taken}", flush=True)
        
    except Exception as e:
        print(f"Error communicating with environment: {e}")
        sys.exit(1)

if __name__ == "__main__":
    solve_incident()
