from engine.db.connection import get_connection

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS uploads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            arquivo_nome TEXT NOT NULL,
            data_upload DATETIME DEFAULT CURRENT_TIMESTAMP,
            linhas_inseridas INTEGER NOT NULL,
            observacao TEXT
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            upload_id INTEGER NOT NULL,
            data_venda DATE NOT NULL,
            produto TEXT NOT NULL,
            categoria TEXT NOT NULL,
            preco_unitario REAL NOT NULL,
            quantidade INTEGER NOT NULL,
            canal_venda TEXT NOT NULL,
            vendedor TEXT NOT NULL,
            valor_total REAL NOT NULL
        );
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
