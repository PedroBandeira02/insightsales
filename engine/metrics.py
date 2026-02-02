import pandas as pd

def calcula_faturamento_total (df):
    faturamento_total = (df['quantidade'] * df['preco_unitario']).sum()
    return faturamento_total

def calcula_faturamento_por_produto (df):
    faturamento = df['quantidade'] * df['preco_unitario']
    return faturamento.groupby(df['produto']).sum()

def calcula_ticket_medio (df):
    faturamento = df['quantidade'] * df['preco_unitario']
    return faturamento.mean()

def calcula_quantidade_por_categoria_produto (df):
    quantidade_por_produto = df.groupby(['categoria', 'produto'])['quantidade'].sum()
    return quantidade_por_produto

def calcula_canal_mais_utilizado (df):
    canal_mais_utilizado = df['canal_venda'].value_counts().idxmax()
    return canal_mais_utilizado

def calcula_faturamento_por_vendedor (df):
    faturamento_por_vendedor = df['quantidade'] * df['preco_unitario']
    return faturamento_por_vendedor.groupby(df['vendedor']).sum()

def faturamento_e_vendas_por_mes(df):
    df_temp = df.copy()
    df_temp['faturamento'] = df_temp['quantidade'] * df_temp['preco_unitario']

    resumo = df_temp.groupby(
        pd.Grouper(key='data_venda', freq='ME')
    ).agg(
        faturamento_total=('faturamento', 'sum'),
        numero_vendas=('faturamento', 'count')
    )

    return resumo


