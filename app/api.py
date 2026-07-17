from fastapi import APIRouter
from app.schemas import FormulaInput, FormulaOutput
from processing.features import prepare_input
from processing.data_manager import load_model

api_router = APIRouter()
model = load_model()

@api_router.get("/health")
def health():
    return {"status": "ok"}

@api_router.post("/predict", response_model=FormulaOutput)
def predict(input_data: FormulaInput):
    df = prepare_input(input_data.dict())
    prediction = model.predict(df)[0]
    return FormulaOutput(total_revenue_usd_m=round(float(prediction), 2))