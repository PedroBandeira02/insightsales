import pandas as pd

def variacao_absoluta(series: pd.Series) -> pd.Series:
    return series.diff()

def variacao_percentual (series: pd.Series) -> pd.Series:
    return series.pct_change()

def coeficiente_variacao(series: pd.Series) -> float | None:
    media = series.mean()
    if media == 0:
        return None
    return series.std() / media

def indice_volatilidade(series: pd.Series) -> float:
    variacao_pct = series.pct_change().dropna()
    return variacao_pct.std()

def media_movel(series: pd.Series, janela: int = 3) -> pd.Series:
    return series.rolling(window=janela).mean()



    