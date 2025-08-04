from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class InferenceRequest(BaseModel):
    file_path: str

@router.post("/inference/player")
def run_inference(req: InferenceRequest):
    # Placeholder logic before dummy model was added
    return {
        "message": f"Inference would be run on: {req.file_path}"
    }

