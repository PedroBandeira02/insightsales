def regra_volatilidade(volatilidade: float) -> dict:
    if volatilidade <= 0.20:
        nivel = "baixo"
        risco = False
    elif volatilidade <= 0.30:
        nivel = "moderado"
        risco = False
    else:
        nivel = "alto"
        risco = True

    return {
        "nivel": nivel,
        "risco": risco
    }

def regra_previsibilidade(cv: float | None) -> dict:
    if cv is None:
        return {
            "nivel": "indefinido",
            "risco": True
        }

    if cv <= 0.15:
        nivel = "previsivel"
        risco = False
    elif cv <= 0.30:
        nivel = "moderado"
        risco = False
    else:
        nivel = "imprevisivel"
        risco = True

    return {
        "nivel": nivel,
        "risco": risco
    }

import pandas as pd

def regra_quedas_consecutivas(
    variacao_pct: pd.Series,
    limite: int = 2
) -> dict:
    """
    Avalia se há quedas consecutivas na variação percentual.
    """
    if variacao_pct is None or variacao_pct.empty:
        return {
            "nivel": "indefinido",
            "risco": False
        }

    # True para períodos de queda
    quedas = variacao_pct < 0

    # Conta sequências consecutivas de quedas
    max_consecutivas = (
        quedas
        .astype(int)
        .groupby((quedas != quedas.shift()).cumsum())
        .sum()
        .max()
    )

    if max_consecutivas >= limite:
        return {
            "nivel": "recorrente",
            "risco": True,
            "qtd_quedas_consecutivas": int(max_consecutivas)
        }

    return {
        "nivel": "isolada",
        "risco": False,
        "qtd_quedas_consecutivas": int(max_consecutivas)
    }

def regra_pico_atipico(
    valor_atual: float,
    media_historica: float,
    desvio_historico: float,
    multiplicador: float = 2.5
) -> dict:
    """
    Avalia se o valor atual representa um pico atípico.
    """
    if desvio_historico == 0:
        return {
            "nivel": "indefinido",
            "risco": False
        }

    limite_superior = media_historica + multiplicador * desvio_historico

    if valor_atual > limite_superior:
        return {
            "nivel": "pico_atipico",
            "risco": True
        }

    return {
        "nivel": "normal",
        "risco": False
    }

