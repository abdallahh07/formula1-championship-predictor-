from xgboost import XGBRegressor

def create_pipeline() -> XGBRegressor:
    model = XGBRegressor(
        random_state=42,
        max_depth=3,
        n_estimators=50,
        learning_rate=0.05,
        subsample=0.8
    )
    return model
  
  