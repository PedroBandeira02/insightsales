import pandas as pd

def temporal_train_test_split(
    df: pd.DataFrame,
    coluna_alvo: str = 'risco_queda_faturamento',
    test_size: float = 0.20,
    coluna_data: str = 'data_venda'
):
    if coluna_data not in df.columns:
        raise KeyError(f"Coluna de data '{coluna_data}' não encontrada.")

    if coluna_alvo not in df.columns:
        raise KeyError(f"Variável alvo '{coluna_alvo}' não encontrada.")

    if not 0 < test_size < 1:
        raise ValueError("test_size deve estar entre 0 e 1.")

    df = df.copy()
    df[coluna_data] = pd.to_datetime(df[coluna_data])

    df = df.sort_values(by=coluna_data).reset_index(drop=True)

    split_index = int(len(df) * (1 - test_size))

    X_train = df.iloc[:split_index].drop(columns=[coluna_alvo, coluna_data])
    y_train = df.iloc[:split_index][coluna_alvo]

    X_test = df.iloc[split_index:].drop(columns=[coluna_alvo, coluna_data])
    y_test = df.iloc[split_index:][coluna_alvo]

    return X_train, X_test, y_train, y_test

