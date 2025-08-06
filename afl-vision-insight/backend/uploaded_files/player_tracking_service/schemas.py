from pydantic import BaseModel
from typing import List, Dict

class InferenceRequest(BaseModel):
    file_path: str

class PlayerDetection(BaseModel):
    player_id: str
    bbox: List[int]
    center: List[int]
    confidence: float
    width: int
    height: int

class InferenceResponse(BaseModel):
    status: str
    message: str
    video_info: Dict[str, str]
    tracking_results: List[PlayerDetection]
