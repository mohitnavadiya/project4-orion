# player_tracking_service/app/main.py

from fastapi import FastAPI, UploadFile, File, HTTPException
from app.tracker import PlayerTracker
from app.models import PlayerTrackingResponse  # ✅ Import model
import os
import uuid
import shutil

app = FastAPI(title="Player Tracking Microservice")
tracker = PlayerTracker()

UPLOAD_DIR = "uploaded_videos"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/track-players", response_model=PlayerTrackingResponse)
async def track_players(video: UploadFile = File(...)):
    try:
        file_id = str(uuid.uuid4())
        video_path = os.path.join(UPLOAD_DIR, f"{file_id}_{video.filename}")

        with open(video_path, "wb") as f:
            shutil.copyfileobj(video.file, f)

        result = tracker.process_video(video_path)
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
