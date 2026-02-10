import pandas as pd
import numpy as np

def ordenacao_temporal (df: pd.DataFrame, coluna_temporal:str = 'data_venda') -> pd.DataFrame:
    df = df.copy()
    df[coluna_temporal] = pd.to_datetime(df[coluna_temporal])
    df = df.sort_values(by= coluna_temporal)
    df = df.reset_index(drop=True)
    return df

import pandas as pd

def media_faturamento_ultimos_periodos(
    df: pd.DataFrame,
    coluna_faturamento: str = 'faturamento',
    janela: int = 3
) -> pd.DataFrame:
    df = df.copy()

    nome_coluna = f'fat_media_{janela}p'

    df[nome_coluna] = (
        df[coluna_faturamento]
        .rolling(window=janela, min_periods=janela)
        .mean()
    )

    return df

def volatilidade_faturamento(
    df: pd.DataFrame,
    coluna_faturamento: str = 'faturamento',
    janela: int = 3
) -> pd.DataFrame:
    
    df = df.copy()

    variacao_pct = df[coluna_faturamento].pct_change()

    nome_coluna = f'fat_volatilidade_{janela}p'

    df[nome_coluna] = (
        variacao_pct
        .rolling(window=janela, min_periods=janela)
        .std()
    )

    return df
            
def tendencia_faturamento (df: pd.DataFrame, coluna_faturamento: str = 'faturamento', janela: int = 3) -> pd.DataFrame:
    df = df.copy()

    media_passada = (
        df['faturamento']
        .rolling(window=3, min_periods=3)
        .mean()
        .shift(1)
    )

    df['fat_tendencia'] = (df['faturamento'] - media_passada) / media_passada

    return df

def concentracao_faturamento_top_n(
    df: pd.DataFrame,
    coluna_data: str = 'data_venda',
    coluna_faturamento: str = 'faturamento',
    coluna_clientes: str = 'id_clientes',
    top_n: int = 3
) -> pd.DataFrame:

    df = df.copy()

    df[coluna_data] = pd.to_datetime(df[coluna_data])

    faturamento_cliente_mes = (
        df
        .groupby(
            [pd.Grouper(key=coluna_data, freq='M'), coluna_clientes]
        )[coluna_faturamento]
        .sum()
        .reset_index()
    )

    faturamento_total_mes = (
        faturamento_cliente_mes
        .groupby(coluna_data)[coluna_faturamento]
        .sum()
        .reset_index(name='fat_total_mes')
    )

    top_n_por_mes = (
        faturamento_cliente_mes
        .sort_values(
            by=[coluna_data, coluna_faturamento],
            ascending=[True, False]
        )
        .groupby(coluna_data)
        .head(top_n)
    )

    faturamento_top_n_mes = (
        top_n_por_mes
        .groupby(coluna_data)[coluna_faturamento]
        .sum()
        .reset_index(name='fat_top_n_mes')
    )

    concentracao = (
        faturamento_total_mes
        .merge(faturamento_top_n_mes, on=coluna_data)
    )

    concentracao['fat_concentracao_top_n'] = (
        concentracao['fat_top_n_mes'] / concentracao['fat_total_mes']
    )

    return concentracao[[coluna_data, 'fat_concentracao_top_n']]

def risco_queda_faturamento(
    df: pd.DataFrame,
    coluna_faturamento: str = 'faturamento',
    janela: int = 3,
    limite_queda: float = 0.10
) -> pd.DataFrame:

    df = df.copy()

    media_passada = (
        df[coluna_faturamento]
        .rolling(window=janela, min_periods=janela)
        .mean()
    )

    faturamento_futuro = df[coluna_faturamento].shift(-1)

    df['risco_queda_faturamento'] = np.where(
        faturamento_futuro < (1 - limite_queda) * media_passada,
        1,
        0
    )

    return df

def build_features(
    df: pd.DataFrame,
    coluna_data: str = 'data_venda'
) -> pd.DataFrame:

    df = ordenacao_temporal(df, coluna_data)

    df = media_faturamento_ultimos_periodos(df)
    df = tendencia_faturamento(df)
    df = volatilidade_faturamento(df)

    return df









  


