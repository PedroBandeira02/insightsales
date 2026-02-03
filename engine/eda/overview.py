"""
O que este módulo analisa?

Este módulo fornece uma visão geral do dataset após a limpeza,
com o objetivo de entender sua estrutura básica e limites analíticos.

Ele responde perguntas como:
- Quantas linhas e colunas existem?
- Qual período temporal é coberto pelos dados?
- Quais tipos de variáveis estão disponíveis?
- Há lacunas relevantes ou dados insuficientes?
- O dataset é adequado para análises mais profundas?

O que este módulo NÃO faz:
- Não calcula métricas finais
- Não analisa distribuições detalhadas
- Não avalia crescimento ou tendências
- Não gera conclusões de negócio

Seu papel é orientar e validar as análises posteriores.
"""
import pandas as pd


def dataset_overview(df: pd.DataFrame) -> dict:
    """
    Gera uma visão geral do dataset para avaliar sua estrutura
    e adequação para análises exploratórias mais profundas.
    """

    overview = {}

    # Tamanho do dataset
    overview["num_linhas"] = df.shape[0]
    overview["num_colunas"] = df.shape[1]

    # Tipos de colunas
    overview["tipos_colunas"] = df.dtypes.astype(str).to_dict()

    # Colunas com valores nulos
    overview["valores_nulos"] = df.isnull().sum().to_dict()

    # Colunas numéricas e categóricas
    overview["colunas_numericas"] = df.select_dtypes(include="number").columns.tolist()
    overview["colunas_categoricas"] = df.select_dtypes(exclude="number").columns.tolist()

    # Alerta de dataset pequeno
    overview["alerta_dataset_pequeno"] = overview["num_linhas"] < 30

    return overview
