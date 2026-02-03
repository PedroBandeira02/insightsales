import sys
from pathlib import Path

# Garante que a raiz do projeto esteja no PYTHONPATH
ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT_DIR))

from engine.load_data import read_csv, standardize_columns
from engine.clean_data import clean_df

from engine.eda.temporal import analise_temporal
from engine.eda.distribution import (
    distribuicao_por_produto,
    distribuicao_por_vendedor,
    distribuicao_por_canal
)

from engine.insights.generator import gerar_insights


def main():
    path = "data/raw/vendas_exemplo.csv"

    # =========================
    # ETAPA 1 — PREPARAÇÃO (MÊS 2)
    # =========================
    df = read_csv(path)
    df = standardize_columns(df)
    df = clean_df(df)

    # =========================
    # ETAPA 2 — EDA (MÊS 3)
    # =========================
    resultado_temporal = analise_temporal(df, coluna_data="data_venda")

    dist_produto = distribuicao_por_produto(df)
    dist_vendedor = distribuicao_por_vendedor(df)
    dist_canal = distribuicao_por_canal(df)

    # =========================
    # ETAPA 3 — INSIGHTS (MÊS 3)
    # =========================
    insights = gerar_insights(
        resultado_temporal,
        dist_produto,
        dist_vendedor,
        dist_canal
    )

    # =========================
    # SAÍDA FINAL
    # =========================
    print("\n🧠 INSIGHTS GERADOS\n")

    for i, insight in enumerate(insights, start=1):
        print(f"{i}. {insight}")


if __name__ == "__main__":
    main()



