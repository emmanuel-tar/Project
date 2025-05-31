import sqlite3


def init_db():
    conn = sqlite3.connect("data/budget.db")
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            amount REAL,
            category TEXT,
            note TEXT,
            type TEXT
        )
    """
    )
    conn.commit()
    conn.close()
