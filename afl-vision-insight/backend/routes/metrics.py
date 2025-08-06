from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime
import random

router = APIRouter()

class PlayerInferenceResponse(BaseModel):
    label: str
    confidence: float
    timestamp: str

metrics_store = {
    "player_inference_calls": 0,
    "last_player_result": None
}

@router.post("/player", response_model=PlayerInferenceResponse)
async def infer_player():
    result = {
        "label": "player",
        "confidence": round(random.uniform(0.8, 0.99), 2),
        "timestamp": datetime.utcnow().isoformat()
    }
    metrics_store["player_inference_calls"] += 1
    metrics_store["last_player_result"] = result
    return result

@router.get("/metrics")
def get_metrics():
    return metrics_store
