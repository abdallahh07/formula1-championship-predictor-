from fastapi import FastAPI
from app.api import api_router

app = FastAPI(
    title="Formula 1 Team Revenue Predictor",
    description="Predicts F1 constructor team revenue using financial and performance data (2010-2026).",
    version="1.0.0"
)

app.include_router(api_router)