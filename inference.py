import os
import uvicorn
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI(title="Incident Response AI Environment")


env_state = {
    "is_initialized": False,
    "step_count": 0
}

@app.get("/")
async def root():
    """Provides a friendly message for the Hugging Face UI."""
    return {"message": "Incident Response AI API is running successfully! Use the OpenEnv CLI to interact with this space."}

@app.get("/health")
async def health():
    """Required by OpenEnv to check if the server is running."""
    return {"status": "ok"}

@app.get("/metadata")
async def metadata():
    """Provides environment details to OpenEnv."""
    return {
        "name": "incident-response-AI",
        "description": "AI Incident Response Environment",
        "version": "1.0.0",
        "type": "custom"
    }

@app.post("/reset")
async def reset(request: Request):
    """
    Handles the 'OpenEnv Reset (POST OK)' validation.
    """
    try:
        body = await request.json()
    except Exception:
        body = {}
        
    
    env_state["is_initialized"] = True
    env_state["step_count"] = 0
    
    
   
    
    return JSONResponse(content={
        "observation": "Environment reset. Ready for incident response.",
        "state": env_state
    })

@app.post("/step")
async def step(request: Request):
    """
    Processes an action and returns the observation and reward.
    """
    if not env_state["is_initialized"]:
        raise HTTPException(status_code=400, detail="Must call /reset first.")
        
    try:
        body = await request.json()
    except Exception:
        body = {}
        
    action = body.get("action", {})
    env_state["step_count"] += 1
    
    
    
    return JSONResponse(content={
        "observation": f"Executed action: {action}",
        "reward": 0.0,
        "done": env_state["step_count"] >= 10,
        "truncated": False,
        "info": {"step": env_state["step_count"]},
        "state": env_state
    })

@app.get("/state")
async def state():
    """Returns the current state of the environment."""
    return JSONResponse(content={
        "observation": "Current state snapshot",
        "state": env_state
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))
    uvicorn.run(app, host="0.0.0.0", port=port)
