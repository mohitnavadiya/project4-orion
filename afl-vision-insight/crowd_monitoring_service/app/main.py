# app/main.py

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse
from app.monitor import CrowdMonitor
from app.models import CrowdMonitoringResponse  # ✅ Import your model
import os
import uuid
import shutil

app = FastAPI(title="Crowd Monitoring Microservice")

UPLOAD_DIR = "uploaded_images"
HEATMAP_DIR = "heatmaps"
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(HEATMAP_DIR, exist_ok=True)

monitor = CrowdMonitor()

@app.post("/analyze-crowd/", response_model=CrowdMonitoringResponse)  # ✅ Add response model
async def analyze_crowd(image: UploadFile = File(...)):
    if not image.filename.lower().endswith((".png", ".jpg", ".jpeg")):
        raise HTTPException(status_code=400, detail="Only image files (.jpg, .png) are supported.")

    try:
        file_id = str(uuid.uuid4())
        input_path = os.path.join(UPLOAD_DIR, f"{file_id}_{image.filename}")
        output_path = os.path.join(HEATMAP_DIR, f"{file_id}_heatmap.png")

        with open(input_path, "wb") as f:
            shutil.copyfileobj(image.file, f)

        result = monitor.process_image(input_path, output_path)

        if result["status"] == "error":
            raise HTTPException(status_code=result.get("code", 500), detail=result["message"])

        return {
            "message": result["message"],
            "heatmap_image": f"/get-heatmap/{file_id}_heatmap.png",
            "crowd_estimates": result["crowd_estimates"]
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to analyze image: {str(e)}")

@app.get("/get-heatmap/{filename}")
async def get_heatmap(filename: str):
    path = os.path.join(HEATMAP_DIR, filename)
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="Heatmap not found.")
    return FileResponse(path, media_type="image/png")
