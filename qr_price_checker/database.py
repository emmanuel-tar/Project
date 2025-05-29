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
cur.execute(
    "INSERT INTO items (barcode, name, price, stock) VALUES (?, ?, ?, ?)",
    ("4455667788", "Cocoa Powder", 25500.00, 5),
    
)
def create_table():
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
    conn.commit()
    conn.close()

def insert_item(barcode, name, price, stock):
    conn = sqlite3.connect("data.db")
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO items (barcode, name, price, stock) VALUES (?, ?, ?, ?)",
        (barcode, name, price, stock),
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

def main():
    create_table()
    items = [
        ("1234567890", "Pepsi", 4500.00, 25),
        ("0987654321", "Coca-Cola", 5000.00, 30),
        ("1122334455", "Sprite", 4000.00, 20),
        ("2233445566", "Fanta", 3500.00, 15),
        ("3344556677", "Mountain Dew", 3000.00, 10),
        ("4455667788", "Cocoa Powder", 25500.00, 5),
    ]
    for item in items:
        insert_item(*item)

if __name__ == "__main__":
    main()
conn.commit()
conn.close()
def get_item_by_barcode(barcode):
    conn = sqlite3.connect("data.db")
    cur = conn.cursor()
    cur.execute("SELECT name, price, stock FROM items WHERE barcode = ?", (barcode,))
    item = cur.fetchone()
    conn.close()
    return item