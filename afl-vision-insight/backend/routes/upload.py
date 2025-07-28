from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    return JSONResponse(content={
        "message": "File received successfully",
        "filename": file.filename
    })
