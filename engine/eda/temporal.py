"""
Responsabilidade do módulo temporal.py:

Este módulo analisa o comportamento dos dados ao longo do tempo,
com foco em identificar padrões temporais básicos, como tendência,
regularidade, picos e possíveis sinais de sazonalidade.

Perguntas que este módulo responde:
- O faturamento varia significativamente ao longo do tempo?
- Existem picos isolados que distorcem a média?
- O crescimento observado é consistente ou irregular?
- O volume de vendas acompanha o faturamento?

Perguntas que este módulo NÃO responde:
- Qual decisão de negócio tomar
- Previsão de vendas futuras
- Avaliação de desempenho individual
"""

import pandas as pd

def verificador_de_coluna_temporal(df, coluna_data):
    resultado = {
        "existe_coluna": False,
        "qtd_valores_invalidos": None,
        "valores_adequados": False
    }

    if coluna_data not in df.columns:
        return resultado

    resultado["existe_coluna"] = True

    datas_convertidas = pd.to_datetime(df[coluna_data], errors="coerce")

    qtd_invalidos = datas_convertidas.isna().sum()
    resultado["qtd_valores_invalidos"] = qtd_invalidos

    resultado["valores_adequados"] = qtd_invalidos == 0

    return resultado

def analise_temporal(df_mensal):
    analise = {}
    alertas = []

    # df_mensal já vem com:
    # data_venda | faturamento_total | numero_vendas

    df_mensal = df_mensal.sort_values("data_venda").copy()

    # Variações (isso AINDA é análise, não SQL)
    df_mensal["var_faturamento"] = df_mensal["faturamento_total"].diff()
    df_mensal["var_faturamento_pct"] = df_mensal["faturamento_total"].pct_change()

    df_mensal["var_quantidade"] = df_mensal["numero_vendas"].diff()
    df_mensal["var_quantidade_pct"] = df_mensal["numero_vendas"].pct_change()

    # Alertas (continua igual em espírito)
    std_faturamento = df_mensal["var_faturamento_pct"].dropna().std()
    cv_qtd = df_mensal["numero_vendas"].std() / df_mensal["numero_vendas"].mean()

    if len(df_mensal) < 4:
        alertas.append("Período curto para avaliar estabilidade de crescimento")
    else:
        if std_faturamento > 0.3:
            alertas.append("Crescimento de faturamento irregular ao longo do tempo.")
        if cv_qtd > 0.30:
            alertas.append("Volume apresenta alta variabilidade relativa.")

    picos = df_mensal.sort_values("faturamento_total", ascending=False).head(3)

    analise["temporal"] = df_mensal
    analise["picos_faturamento"] = picos
    analise["alertas"] = alertas

    return analise

   



    

