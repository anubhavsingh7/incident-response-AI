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
    return {"message": "Incident Response AI API is running successfully!"}

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get("/metadata")
async def metadata():
    return {
        "name": "incident-response-AI",
        "description": "AI Incident Response Environment",
        "version": "1.0.0",
        "type": "custom"
    }

@app.post("/reset")
async def reset(request: Request):
    env_state["is_initialized"] = True
    env_state["step_count"] = 0
    return JSONResponse(content={
        "observation": "Environment reset.",
        "state": env_state
    })

@app.post("/step")
async def step(request: Request):
    if not env_state["is_initialized"]:
        raise HTTPException(status_code=400, detail="Must call /reset first.")
    env_state["step_count"] += 1
    return JSONResponse(content={
        "observation": "Executed action",
        "reward": 0.0,
        "done": env_state["step_count"] >= 10,
        "truncated": False,
        "info": {"step": env_state["step_count"]},
        "state": env_state
    })

@app.get("/state")
async def state():
    return JSONResponse(content={"observation": "State snapshot", "state": env_state})


def main():
    port = int(os.environ.get("PORT", 7860))
    uvicorn.run("server.app:app", host="0.0.0.0", port=port)
