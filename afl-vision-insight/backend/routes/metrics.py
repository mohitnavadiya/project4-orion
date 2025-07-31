from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/")
async def get_metrics():
    metrics_data = {
        "total_requests": 5,
        "success_rate": "100%",
        "average_response_time_ms": 120,
        "uptime": "3 hours 20 minutes"
    }
    return JSONResponse(content=metrics_data)