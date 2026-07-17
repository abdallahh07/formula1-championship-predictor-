import pandas as pd
from processing.data_manager import load_model
from processing.features import prepare_input


def make_prediction(input_data: dict) -> dict:
    model = load_model()
    df = prepare_input(input_data)
    prediction = model.predict(df)[0]

    return {
        "predicted_revenue_usd_m": round(float(prediction), 2)
    }


if __name__ == "__main__":
    sample = {
        "season": 2024,
        "operating_budget_usd_m": 400.0,
        "sponsorship_revenue_usd_m": 150.0,
        "prize_money_usd_m": 120.0,
        "in_cost_cap_era": 1,
        "cost_cap_limit_usd_m": 135.0,
        "is_constructors_champion": 0,
        "team_name_encoded": 4,
        "country_iso3_encoded": 2
    }

    result = make_prediction(sample)
    print(result)