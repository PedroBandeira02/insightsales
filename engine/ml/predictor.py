import pandas as pd

def baseline_persistencia(y_train: pd.Series, tamanho_teste: int) -> pd.Series:
    ultimo_valor = y_train.iloc[-1]
    return pd.Series([ultimo_valor] * tamanho_teste)


def baseline_frequencia(y_train: pd.Series, tamanho_teste: int) -> pd.Series:
    valor = y_train.mode()[0]
    return pd.Series([valor] * tamanho_teste)

