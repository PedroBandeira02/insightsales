import pandas as pd


def participacao_percentual(series: pd.Series) -> pd.Series:
    total = series.sum()

    if total == 0:
        return series * 0

    return series / total


def participacao_acumulada(series: pd.Series) -> pd.Series:
    participacao = participacao_percentual(series)
    return participacao.sort_values(ascending=False).cumsum()


def top_n_participacao(series: pd.Series, n: int = 3) -> float:
    participacao = participacao_percentual(series)
    return participacao.sort_values(ascending=False).head(n).sum()
