from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.connection import engine

app = FastAPI(
    title="Intelligent Emergency Response API",
    description="Backend API for emergency response and ambulance routing system",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {
        "message": "Intelligent Emergency Response API is running",
        "version": "0.1.0"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.get("/database-health")
def database_health():
    try:
        with engine.connect() as connection:
            return {
                "database": "connected"
            }
    except Exception as e:
        return {
            "database": "disconnected",
            "error": str(e)
        }