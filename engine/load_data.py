import pandas as pd

def read_csv (path):   
    df_vendas = pd.read_csv(path, skipinitialspace= True, na_values= ['?', 'NA', 'N/A'], encoding= 'UTF-8')
    return df_vendas

def standardize_columns (df_lido):
    colunas_padronizadas = df_lido.columns.str.lower().str.strip().str.replace(' ', '_')
    df_lido.columns = colunas_padronizadas
    return df_lido


