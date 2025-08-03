from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import time
import random

router = APIRouter()

class InferenceInput(BaseModel):
    file_path: str

@router.post("/inference/")
def run_inference(data: InferenceInput):
    try:
        # Simulate model processing
        time.sleep(1)
        return {
            "file": data.file_path,
            "prediction": random.choice(["Player Detected", "Ball Detected", "No Detection"]),
            "confidence": round(random.uniform(0.6, 0.95), 2)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
