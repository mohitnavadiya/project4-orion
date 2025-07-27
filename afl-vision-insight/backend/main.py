from fastapi import FastAPI
from routes import upload, inference, metrics
from config.cors import add_cors  # custom CORS setup

app = FastAPI()

# Apply CORS middleware
add_cors(app)

# Health check
@app.get("/")
def read_root():
    return {"message": "AFL Vision Backend Running"}

# Register routers
app.include_router(upload.router, prefix="/upload", tags=["Upload"])
app.include_router(inference.router, prefix="/inference", tags=["Inference"])
app.include_router(metrics.router, prefix="/metrics", tags=["Metrics"])