from engine.load_data import read_csv, standardize_columns
from engine.clean_data import clean_df
from engine.metrics import (
    calcula_faturamento_total,
    calcula_faturamento_por_produto,
    calcula_ticket_medio,
    calcula_quantidade_por_categoria_produto,
    calcula_canal_mais_utilizado,
    calcula_faturamento_por_vendedor,
    faturamento_e_vendas_por_mes
)

def main():
    path = "data/raw/vendas_exemplo.csv"

    df = read_csv(path)
    df = standardize_columns(df)

    df = clean_df(df)

    faturamento_total = calcula_faturamento_total(df)
    ticket_medio = calcula_ticket_medio(df)
    canal_mais_utilizado = calcula_canal_mais_utilizado(df)

    faturamento_produto = calcula_faturamento_por_produto(df)
    faturamento_vendedor = calcula_faturamento_por_vendedor(df)
    quantidade_categoria_produto = calcula_quantidade_por_categoria_produto(df)
    resumo_mensal = faturamento_e_vendas_por_mes(df)

    print("\n📊 INSIGHTSALES — RESUMO GERAL\n")

    print(f"💰 Faturamento total: R$ {faturamento_total:,.2f}")
    print(f"🧾 Ticket médio: R$ {ticket_medio:,.2f}")
    print(f"🛒 Canal mais utilizado: {canal_mais_utilizado}")

    print("\n📦 Faturamento por produto:")
    print(faturamento_produto)

    print("\n👤 Faturamento por vendedor:")
    print(faturamento_vendedor)

    print("\n📊 Quantidade vendida por categoria e produto:")
    print(quantidade_categoria_produto)

    print("\n📅 Resumo mensal (faturamento e número de vendas):")
    print(resumo_mensal)

if __name__ == "__main__":
    main()
