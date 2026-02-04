from engine.load_data import load_data
from engine.clean_data import clean_data

from engine.db.schema import create_tables
from engine.db.ingest import register_upload, insert_sales
from engine.db.queries import sales_over_time, sales_by_category

from engine.eda.temporal import analise_temporal
from engine.eda.distribution import distribuicao_por_categoria


def main():
    # 1. Garante que o schema exista
    create_tables()

    # 2. Carrega os dados brutos
    df_raw = load_data("data/raw/vendas_exemplo.csv")

    # 3. Limpa os dados
    df_clean = clean_data(df_raw)

    # 4. Registra o upload
    upload_id = register_upload(
        arquivo_nome="vendas_exemplo.csv",
        linhas_inseridas=len(df_clean),
        observacao="Carga inicial do InsightSales"
    )

    # 5. Insere as vendas no banco
    insert_sales(df_clean, upload_id)

    # 6. Query SQL → análise temporal
    df_temporal = sales_over_time()
    resultado_temporal = analise_temporal(df_temporal)

    print("\n📊 Análise Temporal — Alertas:")
    for alerta in resultado_temporal["alertas"]:
        print(f"- {alerta}")

    print("\n🔥 Picos de faturamento:")
    print(resultado_temporal["picos_faturamento"])

    # 7. Query SQL → distribuição por categoria
    df_categoria = sales_by_category()
    resultado_dist = distribuicao_por_categoria(df_categoria)

    print("\n📊 Distribuição de faturamento por categoria — Alertas:")
    for alerta in resultado_dist["alertas"]:
        print(f"- {alerta}")

    print("\n🏆 Ranking de faturamento por categoria:")
    print(resultado_dist["faturamento_por_dimensao"])


if __name__ == "__main__":
    main()







