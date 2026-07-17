import joblib
from pathlib import Path
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, LabelEncoder
from xgboost import XGBRegressor
from pipeline import create_pipeline
from processing.data_manager import save_model
from config.config import FEATURES, TARGET, DROP_FEATURES


def run_training():
    print("Starting training pipeline...")

    # 1. Load data
    construction = pd.read_csv("data/constructor_finances.csv")
    print("Data loaded successfully")

    # 2. Preprocessing
    construction["cost_cap_limit_usd_m"] = construction["cost_cap_limit_usd_m"].fillna(0)
    le = LabelEncoder()
    construction["team_name_encoded"] = le.fit_transform(construction["team_name"])
    construction["country_iso3_encoded"] = le.fit_transform(construction["country_iso3"])

    # 3. Define X and y
    x = construction.drop(columns=DROP_FEATURES)
    y = construction[TARGET]

    # 4. Chronological split
    split_idx = int(len(construction) * 0.80)
    x_train = x.iloc[:split_idx]
    x_test = x.iloc[split_idx:]
    y_train = y.iloc[:split_idx]
    y_test = y.iloc[split_idx:]

    # 5. Train
    model = create_pipeline()
    model.fit(x_train, y_train)

    # 6. Evaluate
    y_pred = model.predict(x_test)
    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))

    print(f"R2: {r2:.4f}")
    print(f"MAE: {mae:.4f}")
    print(f"RMSE: {rmse:.4f}")

    save_model(model,"final_xgb.pkl")
    joblib.dump(X_train.columns.tolist(), "trained_model/feature_names.pkl")
    print("Model saved successfully")


if __name__ == "__main__":
    run_training()