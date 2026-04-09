import requests
import time
import sys

BASE_URL = "http://localhost:7860"

def solve_incident():
    task_name = "suspicious_login_investigation"
    
    print(f"[START] task={task_name}", flush=True)
    
    try:
        time.sleep(2)
        
        reset_response = requests.post(f"{BASE_URL}/reset", json={}).json()
        
        total_reward = 0.0
        steps_taken = 0
        
        for i in range(5):
            steps_taken += 1
            
            simulated_action = {"command": f"check_ip_logs_step_{i}"}
            
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
