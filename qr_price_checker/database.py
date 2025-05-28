import sqlite3

conn = sqlite3.connect("data.db")
cur = conn.cursor()
cur.execute(
    """
CREATE TABLE IF NOT EXISTS items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    barcode TEXT,
    name TEXT,
    price REAL,
    stock INTEGER
)
"""
)
# Insert sample item
cur.execute(
    "INSERT INTO items (barcode, name, price, stock) VALUES (?, ?, ?, ?)",
    ("1234567890", "Pepsi", 4500.00, 25),
)
cur.execute(
    "INSERT INTO items (barcode, name, price, stock) VALUES (?, ?, ?, ?)",
    ("0987654321", "Coca-Cola", 5000.00, 30),
)
cur.execute(
    "INSERT INTO items (barcode, name, price, stock) VALUES (?, ?, ?, ?)",
    ("1122334455", "Sprite", 4000.00, 20),
)
cur.execute(
    "INSERT INTO items (barcode, name, price, stock) VALUES (?, ?, ?, ?)",
    ("2233445566", "Fanta", 3500.00, 15),
)
cur.execute(
    "INSERT INTO items (barcode, name, price, stock) VALUES (?, ?, ?, ?)",
    ("3344556677", "Mountain Dew", 3000.00, 10),
)
conn.commit()
conn.close()
def get_item_by_barcode(barcode):
    conn = sqlite3.connect("data.db")
    cur = conn.cursor()
    cur.execute("SELECT name, price, stock FROM items WHERE barcode = ?", (barcode,))
    item = cur.fetchone()
    conn.close()
    return item