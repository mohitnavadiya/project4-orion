# backend/uploaded_files/player_tracking_service/main.py

from fastapi import FastAPI
from .schemas import InferenceRequest, InferenceResponse
from .model import run_dummy_inference

app = FastAPI(title="Player Tracking Microservice")

@app.post("/inference/player", response_model=InferenceResponse)
def infer_player(request: InferenceRequest):
    result = run_dummy_inference(request.file_path)
    return result

@app.get("/ping")
async def ping():
    return {"status": "running"}
