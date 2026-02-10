import pandas as pd

def regra_dependencia_unica(
    participacao: pd.Series,
    limite: float = 0.40
) -> dict:

    if participacao is None or participacao.empty:
        return {
            "nivel": "indefinido",
            "risco": False
        }

    maior_participacao = participacao.max()

    if maior_participacao > limite:
        return {
            "nivel": "alta",
            "risco": True,
            "valor": float(maior_participacao)
        }

    return {
        "nivel": "normal",
        "risco": False,
        "valor": float(maior_participacao)
    }


def regra_concentracao_top_n(
    participacao: pd.Series,
    n: int = 3,
    limite: float = 0.70
) -> dict:

    if participacao is None or participacao.empty:
        return {
            "nivel": "indefinido",
            "risco": False
        }

    concentracao_top_n = (
        participacao
        .sort_values(ascending=False)
        .head(n)
        .sum()
    )

    if concentracao_top_n > limite:
        return {
            "nivel": "alta",
            "risco": True,
            "valor": float(concentracao_top_n)
        }

    return {
        "nivel": "normal",
        "risco": False,
        "valor": float(concentracao_top_n)
    }

