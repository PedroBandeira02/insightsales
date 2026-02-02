import pandas as pd
from datetime import datetime

text_cols = ['produto', 'categoria', 'canal_venda','vendedor']
numeric_cols = ['preco_unitario', 'quantidade']
def clean_df (df):
    df = df.drop_duplicates()
    df = df.dropna(how= 'all')
    df['data_venda'] = pd.to_datetime(df['data_venda'], errors= 'coerce')
    for i in text_cols:
        df[i] = df[i].astype('string')
    for j in numeric_cols:
        df[j] = pd.to_numeric(df[j], errors= 'coerce')
    df.loc[df['preco_unitario'] < 0, 'preco_unitario'] = pd.NA
    today = pd.Timestamp(datetime.today().date())
    df.loc[df['quantidade'] <= 0, 'quantidade'] = pd.NA
    df.loc[df['data_venda'] > today, 'data_venda'] = pd.NaT
    return df


