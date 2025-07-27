from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

def add_cors(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # In production, replace "*" with your frontend domain
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
