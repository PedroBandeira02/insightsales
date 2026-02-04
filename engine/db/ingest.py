from engine.db.connection import get_connection


def register_upload(arquivo_nome: str, linhas_inseridas: int, observacao: str = None) -> int:
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO uploads (arquivo_nome, linhas_inseridas, observacao)
        VALUES (?, ?, ?);
    """, (arquivo_nome, linhas_inseridas, observacao))

    upload_id = cursor.lastrowid

    conn.commit()
    conn.close()

    return upload_id


def insert_sales(df, upload_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    sales_data = [
        (
            upload_id,
            row["data_venda"].strftime("%Y-%m-%d"),
            row["produto"],
            row["categoria"],
            row["preco_unitario"],
            row["quantidade"],
            row["canal_venda"],
            row["vendedor"],
            row["preco_unitario"] * row["quantidade"]
        )
        for _, row in df.iterrows()
    ]

    cursor.executemany("""
        INSERT INTO sales (
            upload_id,
            data_venda,
            produto,
            categoria,
            preco_unitario,
            quantidade,
            canal_venda,
            vendedor,
            valor_total
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
    """, sales_data)

    conn.commit()
    conn.close()
