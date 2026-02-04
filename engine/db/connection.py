import sqlite3
from pathlib import Path

DB_PATH = Path("data/database/insightsales.db")

def get_connection():
    return sqlite3.connect(DB_PATH)

if __name__ == "__main__":
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT 1;")
    print(cursor.fetchone())

    conn.close()
