import pandas as pd
from engine.db.connection import get_connection


def sales_over_time():
    """
    Retorna faturamento total e número de vendas por dia.
    """
    query = """
        SELECT
            data_venda,
            SUM(valor_total) AS faturamento_total,
            SUM(quantidade) AS numero_vendas
        FROM sales
        GROUP BY data_venda
        ORDER BY data_venda;
    """

    conn = get_connection()
    df = pd.read_sql_query(query, conn)
    conn.close()

    return df

def sales_by_category():
    query = """
        SELECT
            categoria,
            SUM(valor_total) AS faturamento_total
        FROM sales
        GROUP BY categoria
        ORDER BY faturamento_total DESC;
    """

    conn = get_connection()
    df = pd.read_sql_query(query, conn)
    conn.close()

    return df
