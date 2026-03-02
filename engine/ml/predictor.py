import joblib
import numpy as np
import pandas as pd

from .features import build_regression_dataset


def load_model(path="engine/ml/modelo_regressao_insightsales.pkl"):
    return joblib.load(path)


def predict_next_variation(df: pd.DataFrame):

    model = load_model()

    df_model = build_regression_dataset(df)

    X = df_model.drop(columns=["target"])

    last_row = X.iloc[[-1]]

    log_return_pred = model.predict(last_row)[0]

    variation_percent = np.exp(log_return_pred) - 1

    return {
        "log_return": float(log_return_pred),
        "variation_percent": float(variation_percent)
    }






















# import pandas as pd

# def baseline_persistencia(y_train: pd.Series, tamanho_teste: int) -> pd.Series:
#     ultimo_valor = y_train.iloc[-1]
#     return pd.Series([ultimo_valor] * tamanho_teste)


# def baseline_frequencia(y_train: pd.Series, tamanho_teste: int) -> pd.Series:
#     valor = y_train.mode()[0]
#     return pd.Series([valor] * tamanho_teste)

