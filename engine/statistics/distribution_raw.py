import pandas as pd


def nucleo_distribuicao(
    df,
    col_dimensao,
    col_faturamento="faturamento_total",
    limiar_unico=0.40,
    limiar_top3=0.70
):
    analise = {}
    alertas = []

    df_temp = df.copy()

    if df_temp.empty:
        analise["alertas"] = ["Distribuição vazia para a dimensão analisada."]
        return analise

    faturamento_por_dimensao = (
        df_temp
        .set_index(col_dimensao)[col_faturamento]
        .sort_values(ascending=False)
    )

    participacao_por_dimensao = faturamento_por_dimensao / faturamento_por_dimensao.sum()
    participacao_acumulada = participacao_por_dimensao.cumsum()

    if participacao_por_dimensao.iloc[0] > limiar_unico:
        alertas.append(f"Alta dependência de um único {col_dimensao}.")

    if participacao_por_dimensao.iloc[:3].sum() > limiar_top3:
        alertas.append(f"Alta concentração de faturamento nos três principais {col_dimensao}s.")

    analise["faturamento_por_dimensao"] = faturamento_por_dimensao
    analise["participacao_por_dimensao"] = participacao_por_dimensao
    analise["participacao_acumulada"] = participacao_acumulada
    analise["alertas"] = alertas

    return analise

def distribuicao_por_categoria(df):
    return nucleo_distribuicao(df, col_dimensao="categoria")
