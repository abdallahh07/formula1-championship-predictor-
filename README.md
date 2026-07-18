# 🏎️ Formula 1 Team Revenue Predictor

> Predicts F1 constructor team revenue using 16 years of financial and performance data (2010-2026).

[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://python.org)
[![XGBoost](https://img.shields.io/badge/Model-XGBoost-green)](https://xgboost.readthedocs.io)
[![FastAPI](https://img.shields.io/badge/API-FastAPI-009688)](https://fastapi.tiangolo.com)
[![Railway](https://img.shields.io/badge/Deployed-Railway-purple)](https://railway.app)
[![R²](https://img.shields.io/badge/R²-0.977-orange)]()

---

## 🚀 Live API

**Base URL:** https://formula1-revenue-predictor-production.up.railway.app

| Endpoint | Method | Description |
|---|---|---|
| `/docs` | GET | Interactive Swagger UI |
| `/health` | GET | API health check |
| `/predict` | POST | Revenue prediction |

---

## 📊 Model Performance

| Metric | Value |
|---|---|
| Algorithm | XGBoost Regressor |
| R² Score | **0.977** |
| MAE | 7.08 USD M |
| RMSE | 9.28 USD M |
| Train Period | 2010–2022 |
| Test Period | 2023–2026 |

---

## 🔍 Features

| Feature | Description |
|---|---|
| season | Racing season year |
| operating_budget_usd_m | Team operating budget (USD M) |
| sponsorship_revenue_usd_m | Sponsorship revenue (USD M) |
| prize_money_usd_m | FIA prize money (USD M) |
| in_cost_cap_era | Whether cost cap regulations apply |
| cost_cap_limit_usd_m | Cost cap limit (USD M) |
| is_constructors_champion | Whether team won constructors championship |
| team_name_encoded | Encoded team name |
| country_iso3_encoded | Encoded country |

---

## 📈 Key Findings

- **Sponsorship revenue** is the strongest predictor of total team revenue
- **Prize money** directly correlates with on-track performance
- **Cost cap era** (post-2021) significantly changed revenue distribution
- **Mercedes and Red Bull** dominate revenue generation across all 16 seasons

---

## 🏗️ Project Structure

```
formula1-championship-predictor/
├── app/
│   ├── api.py            # FastAPI endpoints
│   ├── main.py           # App entry point
│   └── schemas.py        # Input/output schemas
├── config/
│   ├── config.py         # Config loader
│   └── config.yml        # Feature names, model config
├── processing/
│   ├── data_manager.py   # Model load/save
│   └── features.py       # Input transformation
├── trained_model/
│   └── final_xgb.pkl     # Trained XGBoost model
├── charts/               # EDA visualizations
├── research.ipynb        # Full research notebook
├── train_pipeline.py     # Training script
├── predict.py            # Prediction script
└── Dockerfile            # Docker deployment
```

---

## 📡 API Usage

```python
import requests

response = requests.post(
    "https://formula1-revenue-predictor-production.up.railway.app/predict",
    json={
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
)

print(response.json())
# {"total_revenue_usd_m": 387.45}
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Model | XGBoost Regressor |
| API | FastAPI, Uvicorn |
| Deployment | Railway, Docker |
| Data | Kaggle F1 Dataset (2010-2026) |
| Language | Python 3.11 |

---

## 👤 About the Author

**Abdallah Hashad**
Quantitative Finance × Machine Learning

```python
class AbdallahHashad:
    role        = "Machine Learning Engineer"
    location    = "Cairo, Egypt 🇪🇬"
    edge        = "CFA-level valuation + Data Science"

    def building(self):
        return ["end-to-end ML pipelines",
                "tuned gradient boosting models",
                "production FastAPI endpoints"]
```

🌐 Portfolio: [abdallah-hashad.vercel.app](https://abdallah-hashad.vercel.app)
📊 Kaggle: [abdallahhashad0](https://www.kaggle.com/abdallahhashad0)
🐙 GitHub: [abdallahh07](https://github.com/abdallahh07)
