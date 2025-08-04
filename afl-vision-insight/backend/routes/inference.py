from fastapi import APIRouter, UploadFile, File, HTTPException
from pydantic import BaseModel
from datetime import datetime
import time
import random

router = APIRouter()

# In-memory store
metrics_store = {
    "player_inference_calls": 0,
    "last_result": None
}

# Response model
class PlayerInferenceResponse(BaseModel):
    label: str
    confidence: float
    timestamp: str

# Input model
class InferenceInput(BaseModel):
    file_path: str

# Dummy simulation endpoint
@router.post("/simulate")
def run_inference(data: InferenceInput):
    try:
        time.sleep(1)
        return {
            "file": data.file_path,
            "prediction": random.choice(["Player Detected", "Ball Detected", "No Detection"]),
            "confidence": round(random.uniform(0.6, 0.95), 2)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Real-time player inference endpoint
@router.post("/player", response_model=PlayerInferenceResponse)
async def infer_player(file: UploadFile = File(...)):
    result = {
        "label": "player",
        "confidence": 0.92,
        "timestamp": datetime.utcnow().isoformat()
    }
    metrics_store["player_inference_calls"] += 1
    metrics_store["last_result"] = result
    return result
