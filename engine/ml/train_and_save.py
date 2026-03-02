import joblib
import pandas as pd

from .features import build_regression_dataset
from .models import get_models


def train_and_save(df: pd.DataFrame, model_name: str = "linear"):

    df_model = build_regression_dataset(df)

    X = df_model.drop(columns=["target"])
    y = df_model["target"]

    models = get_models()

    if model_name not in models:
        raise ValueError("Modelo não encontrado.")

    model = models[model_name]
    model.fit(X, y)

    # 🔎 Análise dos coeficientes
    print("\nCoeficientes do modelo:")
    for feature, coef in zip(X.columns, model.coef_):
        print(f"{feature}: {coef:.6f}")

    joblib.dump(model, "engine/ml/modelo_regressao_insightsales.pkl")

    print(f"\nModelo '{model_name}' salvo com sucesso.")