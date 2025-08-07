from fastapi import APIRouter
from fastapi.responses import JSONResponse
from routes import metrics_store
from pydantic import BaseModel
from datetime import datetime
import random

router = APIRouter()

class PlayerInferenceResponse(BaseModel):
    label: str
    confidence: float
    timestamp: str

@router.post("/player", response_model=PlayerInferenceResponse)
async def infer_player():
    result = {
        "label": "player",
        "confidence": round(random.uniform(0.8, 0.99), 2),
        "timestamp": datetime.utcnow().isoformat()
    }

    metrics_store.player_inference_calls += 1
    metrics_store.last_player_result = result
    return result

@router.get("/metrics/")
async def get_metrics():
    metrics_data = {
        "player_tracking": {
            "calls": metrics_store.player_tracking_calls,
            "last_output": metrics_store.last_player_tracking_output
        },
        "crowd_monitoring": {
            "calls": metrics_store.crowd_monitoring_calls,
            "last_output": metrics_store.last_crowd_monitoring_output
        },
        "inference": {
            "calls": metrics_store.player_inference_calls,
            "last_result": metrics_store.last_player_result
        }
    }
    return JSONResponse(content=metrics_data)
