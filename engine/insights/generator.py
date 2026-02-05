"""
Responsabilidade do módulo generator.py:

Transformar os resultados dos módulos de EDA (temporal e distribution)
em insights textuais objetivos, sem recalcular métricas ou acessar dados brutos.
"""

def gerar_insights(
    resultado_temporal: dict,
    resultado_distribuicao: dict
) -> list[str]:
    """
    Gera insights textuais a partir das regras temporais e de distribuição.
    """
    insights = []

    # ======================================================
    # INSIGHTS TEMPORAIS
    # ======================================================

    volatilidade = resultado_temporal.get("volatilidade", {})
    previsibilidade = resultado_temporal.get("previsibilidade", {})
    quedas = resultado_temporal.get("quedas_consecutivas", {})

    # Volatilidade
    if volatilidade.get("risco"):
        insights.append(
            "O crescimento do faturamento apresenta comportamento irregular ao longo do tempo."
        )
    else:
        insights.append(
            "O crescimento do faturamento apresenta comportamento relativamente estável."
        )

    # Previsibilidade
    if previsibilidade.get("risco"):
        insights.append(
            "O volume de vendas apresenta baixa previsibilidade, indicando instabilidade operacional."
        )
    else:
        insights.append(
            "O volume de vendas apresenta comportamento previsível na maior parte do período."
        )

    # Quedas consecutivas
    if quedas.get("risco"):
        qtd = quedas.get("qtd_quedas_consecutivas", 0)
        insights.append(
            f"Foram identificadas {qtd} quedas consecutivas no crescimento do faturamento."
        )

    # ======================================================
    # INSIGHTS DE DISTRIBUIÇÃO
    # ======================================================

    dependencia = resultado_distribuicao.get("dependencia_unica", {})
    concentracao = resultado_distribuicao.get("concentracao_top_n", {})

    # Dependência única
    if dependencia.get("risco"):
        insights.append(
            "Há alta dependência de um único elemento no faturamento, indicando risco estrutural."
        )
    else:
        insights.append(
            "Não foi identificada dependência excessiva de um único elemento no faturamento."
        )

    # Concentração Top N
    if concentracao.get("risco"):
        insights.append(
            "O faturamento está excessivamente concentrado em poucos elementos."
        )
    else:
        insights.append(
            "A distribuição de faturamento apresenta boa diversificação."
        )

    return insights



