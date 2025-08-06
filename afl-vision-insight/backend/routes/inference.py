# routes/inference.py

from fastapi import APIRouter, File, UploadFile, HTTPException
import os
import uuid
import shutil
import requests

router = APIRouter()
UPLOAD_DIR = "uploaded_files"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# External ML Microservices
PLAYER_TRACKING_URL = "http://localhost:8001/track-players"
CROWD_MONITORING_URL = "http://localhost:8002/analyze-crowd/"

# -------------------------------------
# PLAYER TRACKING (Video input - .mp4)
# -------------------------------------
@router.post("/player-tracking")
async def player_tracking(video: UploadFile = File(...)):
    if not video.filename.endswith(".mp4"):
        raise HTTPException(status_code=400, detail="Only .mp4 video files are allowed.")

    try:
        file_id = str(uuid.uuid4())
        file_path = os.path.join(UPLOAD_DIR, f"{file_id}_{video.filename}")
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(video.file, buffer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"File saving failed: {str(e)}")

    # Forward to player tracking microservice
    try:
        with open(file_path, "rb") as f:
            files = {"video": (video.filename, f, video.content_type)}
            response = requests.post(PLAYER_TRACKING_URL, files=files)

        if response.status_code != 200:
            raise HTTPException(status_code=500, detail="ML service returned an error")

        return response.json()

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to connect to ML service: {str(e)}")


# -------------------------------------
# CROWD MONITORING (Image input - .jpg/.png)
# -------------------------------------
@router.post("/crowd-monitoring")
async def crowd_monitoring(image: UploadFile = File(...)):
    if not image.filename.lower().endswith((".jpg", ".jpeg", ".png")):
        raise HTTPException(status_code=400, detail="Only image files (.jpg/.png) are allowed.")

    try:
        file_id = str(uuid.uuid4())
        file_path = os.path.join(UPLOAD_DIR, f"{file_id}_{image.filename}")
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"File saving failed: {str(e)}")

    # Forward to crowd monitoring microservice
    try:
        with open(file_path, "rb") as f:
            files = {"image": (image.filename, f, image.content_type)}
            response = requests.post(CROWD_MONITORING_URL, files=files)

        if response.status_code != 200:
            raise HTTPException(status_code=500, detail="Crowd monitoring service returned an error")

        return response.json()

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to connect to crowd monitoring service: {str(e)}")
