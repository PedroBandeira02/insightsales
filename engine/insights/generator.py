"""
Responsabilidade do módulo generator.py:

Transformar os resultados dos módulos de EDA (temporal e distribution)
em insights textuais objetivos, sem recalcular métricas ou acessar dados brutos.
"""


def gerar_insights(resultado_temporal, dist_produto, dist_vendedor, dist_canal):

    insights = []

    alertas_temporais = resultado_temporal.get("alertas", [])

    if alertas_temporais:
        for alerta in alertas_temporais:
            insights.append(alerta)
    else:
        insights.append(
            "O faturamento apresentou comportamento relativamente estável no período analisado."
        )

    alertas_produto = dist_produto.get("alertas", [])

    if alertas_produto:
        for alerta in alertas_produto:
            insights.append(alerta)
    else:
        insights.append(
            "A distribuição de faturamento por produto não apresenta concentração relevante."
        )

    alertas_vendedor = dist_vendedor.get("alertas", [])

    if alertas_vendedor:
        for alerta in alertas_vendedor:
            insights.append(alerta)
    else:
        insights.append(
            "A distribuição de faturamento por vendedor não apresenta concentração relevante."
        )

    alertas_canal = dist_canal.get("alertas", [])

    if alertas_canal:
        for alerta in alertas_canal:
            insights.append(alerta)
    else:
        insights.append(
            "A distribuição de faturamento por canal não apresenta concentração relevante."
        )

    return insights

