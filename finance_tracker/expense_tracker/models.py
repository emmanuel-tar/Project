import sqlite3

DB_PATH = "data/budget.db"

def add_transaction(data):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO transactions (date, amount, category, note, type)
        VALUES (?, ?, ?, ?, ?)
    """,
        (data["date"], data["amount"], data["category"], data["note"], data["type"]),
    )
    conn.commit()
    conn.close()


def get_all_transactions():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT * FROM transactions ORDER BY date DESC")
    rows = cur.fetchall()
    conn.close()
    return rows


def get_summary():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT SUM(amount) FROM transactions WHERE type = 'income'")
    income = cur.fetchone()[0] or 0
    cur.execute("SELECT SUM(amount) FROM transactions WHERE type = 'expense'")
    expense = cur.fetchone()[0] or 0
    conn.close()
    return {"income": income, "expense": expense, "net": income - expense}
