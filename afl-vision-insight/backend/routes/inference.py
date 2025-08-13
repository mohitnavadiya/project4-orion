# backend/routes/inference.py

from fastapi import APIRouter, UploadFile, Form, HTTPException
import requests
from backend.routes.metrics_store import metrics_store  # ✅ Safe import

router = APIRouter()

@router.post("/api/v1/inference/player")
async def inference_player(file: UploadFile = None, frame_id: str = Form(None)):
    try:
        if not file and not frame_id:
            raise HTTPException(status_code=400, detail="Either file or frame_id must be provided.")

        url = "http://player_tracking_service:8001/inference/player"

        files = {"file": (file.filename, file.file, file.content_type)} if file else None
        data = {"frame_id": frame_id} if frame_id else None

        response = requests.post(url, files=files, data=data)
        response.raise_for_status()

        result = response.json()
        metrics_store["inference_calls"] += 1

        return {
            "status": "success",
            "data": result.get("tracking_results", [])
        }

    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))
