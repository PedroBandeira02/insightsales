"""
Responsabilidade do módulo distribution.py:

Este módulo analisa a distribuição do faturamento entre categorias
(produtos, vendedores, canais), com o objetivo de identificar
níveis de concentração e dependência.

Perguntas que este módulo responde:
- O faturamento está concentrado em poucos elementos?
- Existe evidência de efeito Pareto?
- A distribuição é equilibrada ou dominada por poucos itens?

Perguntas que este módulo NÃO responde:
- Qual decisão estratégica tomar
- Evolução temporal
- Previsões futuras
"""
import pandas as pd

def nucleo (df, cat_col, limiar_unico= 0.40, limiar_top3= 0.70):
    analise = {}
    deteccao_concentracao = []
    df_temp = df.copy()

    df_temp['faturamento'] = df_temp['quantidade'] * df_temp['preco_unitario']
    faturamento_por_dimensao = df_temp.groupby(cat_col)['faturamento'].sum().sort_values(ascending= False)
    participacao_por_dimensao = faturamento_por_dimensao / faturamento_por_dimensao.sum()
    participacao_acumulada = participacao_por_dimensao.cumsum()

    if faturamento_por_dimensao.empty:
        analise["alertas"] = ["Distribuição vazia para a dimensão analisada."]
        return analise

    if participacao_por_dimensao.iloc[0] > limiar_unico:
        deteccao_concentracao.append(f"Alta dependência de um único {cat_col}.")
    
    if participacao_por_dimensao.iloc[:3].sum() > limiar_top3:
        deteccao_concentracao.append(f"Alta concentração de faturamento nos três principais {cat_col}.")
    
    analise['faturamento_por_dimensao'] = faturamento_por_dimensao
    analise['participacao_por_dimensao'] = participacao_por_dimensao
    analise['participacao_acumulada'] = participacao_acumulada
    analise['alertas'] = deteccao_concentracao

    return analise

def distribuicao_por_produto (df):
    return nucleo (df, cat_col='produto')

def distribuicao_por_vendedor (df):
    return nucleo (df, cat_col='vendedor')

def distribuicao_por_canal (df):
    return nucleo (df, cat_col='canal_venda')
    
