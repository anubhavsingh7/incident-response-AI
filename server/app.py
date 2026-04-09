import os
import uvicorn
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI(title="Real Incident Response Environment")

env_state = {
    "is_initialized": False,
    "step_count": 0,
    "max_steps": 5
}

@app.get("/")
async def root():
    return {"message": "Incident Response Environment is running!"}

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get("/metadata")
async def metadata():
    return {
        "name": "incident-response-AI",
        "version": "1.0.0",
        "type": "custom"
    }

@app.post("/reset")
async def reset(request: Request):
    env_state["is_initialized"] = True
    env_state["step_count"] = 0
    
    return JSONResponse(content={
        "observation": "ALERT: Suspicious login detected from unknown IP. Investigate logs.",
        "state": env_state
    })

@app.post("/step")
async def step(request: Request):
    if not env_state["is_initialized"]:
        raise HTTPException(status_code=400, detail="Must call /reset first.")
        
    try:
        body = await request.json()
    except Exception:
        body = {}
        
    action = body.get("action", {})
    env_state["step_count"] += 1
    
    reward = 0.5 
    is_done = env_state["step_count"] >= env_state["max_steps"]
    
    return JSONResponse(content={
        "observation": f"Processed agent action: {action}",
        "reward": reward,
        "done": is_done,
        "truncated": False,
        "info": {"step": env_state["step_count"]},
        "state": env_state
    })

def main():
    port = int(os.environ.get("PORT", 7860))
    uvicorn.run("server.app:app", host="0.0.0.0", port=port)

if __name__ == "__main__":
    main()
