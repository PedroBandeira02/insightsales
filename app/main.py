from engine.load_data import load_data
from engine.clean_data import clean_data

from engine.db.schema import create_tables
from engine.db.ingest import register_upload, insert_sales
from engine.db.queries import sales_over_time, sales_by_category
from engine.statistics.temporal import (
    variacao_percentual,
    coeficiente_variacao,
    indice_volatilidade
)
from engine.rules.temporal_rules import (
    regra_volatilidade,
    regra_previsibilidade,
    regra_quedas_consecutivas
)
from engine.statistics.distribution import participacao_percentual
from engine.rules.distribution_rules import (
    regra_dependencia_unica,
    regra_concentracao_top_n
)
from engine.insights.generator import gerar_insights


def main():
    # ======================================================
    # INGESTÃO E PERSISTÊNCIA
    # ======================================================

    create_tables()

    df_raw = load_data("data/raw/vendas_exemplo.csv")
    df_clean = clean_data(df_raw)

    upload_id = register_upload(
        arquivo_nome="vendas_exemplo.csv",
        linhas_inseridas=len(df_clean),
        observacao="Carga inicial do InsightSales"
    )

    insert_sales(df_clean, upload_id)

    # ======================================================
    # ANÁLISE TEMPORAL
    # ======================================================

    df_temporal = sales_over_time()

    variacao_pct = variacao_percentual(df_temporal["faturamento_total"])
    volatilidade = indice_volatilidade(df_temporal["faturamento_total"])
    cv_volume = coeficiente_variacao(df_temporal["numero_vendas"])

    resultado_temporal = {
        "volatilidade": regra_volatilidade(volatilidade),
        "previsibilidade": regra_previsibilidade(cv_volume),
        "quedas_consecutivas": regra_quedas_consecutivas(variacao_pct)
    }

    # ======================================================
    # ANÁLISE DE DISTRIBUIÇÃO — CATEGORIA
    # ======================================================

    df_categoria = sales_by_category()

    participacao_categoria = participacao_percentual(
        df_categoria.set_index("categoria")["faturamento_total"]
    )

    resultado_distribuicao = {
        "dependencia_unica": regra_dependencia_unica(participacao_categoria),
        "concentracao_top_n": regra_concentracao_top_n(participacao_categoria)
    }

    # ======================================================
    # GERAÇÃO DE INSIGHTS
    # ======================================================

    insights = gerar_insights(
        resultado_temporal=resultado_temporal,
        resultado_distribuicao=resultado_distribuicao
    )

    print("\n🧠 INSIGHTS GERADOS PELO INSIGHTSALES:\n")
    for insight in insights:
        print(f"- {insight}")


if __name__ == "__main__":
    main()









