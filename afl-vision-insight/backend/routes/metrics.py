from fastapi import APIRouter
import time

router = APIRouter()

@router.get("/metrics/")
def get_metrics():
    # Dummy metrics – you can later hook this to real tracking
    return {
        "model_accuracy": 0.92,
        "avg_inference_time": "1.2s",
        "last_updated": time.strftime("%Y-%m-%d %H:%M:%S")
    }
