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

def analise_temporal (df, coluna_data):
    analise = {}
    alertas = []
    df_temp = df.copy()
    coluna_data_convertida = pd.to_datetime(df[coluna_data], errors= 'coerce')

    valores_nulos = coluna_data_convertida.isna().sum()
    if valores_nulos > 0:
        alertas.append( f"{valores_nulos} registros com data inválida foram ignorados na análise temporal.")

    df_temp["data_convertida"] = coluna_data_convertida
    df_temp = df_temp.dropna(subset=["data_convertida"])
    df_temp['faturamento'] =  df_temp['preco_unitario'] * df_temp['quantidade']

    df_mensal = (df_temp.groupby(pd.Grouper(key= 'data_convertida', freq= 'ME')).agg(faturamento_mensal = ('faturamento', 'sum'), quantidade_mensal = ('quantidade', 'sum')).sort_index())
    df_mensal['var_faturamento'] = df_mensal['faturamento_mensal'].diff()
    df_mensal["var_quantidade"] = df_mensal["quantidade_mensal"].diff()
    df_mensal["var_faturamento_pct"] = df_mensal["faturamento_mensal"].pct_change()
    df_mensal["var_quantidade_pct"] = df_mensal["quantidade_mensal"].pct_change()

    std_faturamento = df_mensal['var_faturamento_pct'].dropna().std()
    cv_qtd = (df_mensal["quantidade_mensal"].std() /df_mensal["quantidade_mensal"].mean())
    if len(df_mensal) < 4:
        alertas.append('Período curto para avaliar estabilidade de crescimento')
    else:
        if std_faturamento > 0.3:
            alertas.append('Crescimento de faturamento irregular ao longo do tempo.')
        if cv_qtd > 0.30:
            alertas.append("Volume mensal apresenta alta variabilidade relativa.")

    picos = df_mensal['faturamento_mensal'].sort_values(ascending= False).head(3)

    analise["mensal"] = df_mensal
    analise["picos_faturamento"] = picos
    analise["alertas"] = alertas

    return analise
   



    

