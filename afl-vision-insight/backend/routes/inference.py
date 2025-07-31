from fastapi import APIRouter

router = APIRouter()

@router.post("/inference")
async def get_inference():
    return { "label": "player", "confidence": 0.85 
