import sqlite3  #Python ka built-in module hai SQLite ko handle karne ke liye

conn = sqlite3.connect("db.sqlite")
cursor = conn.cursor()

cursor.executescript("""
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS orders;

CREATE TABLE customers (
    id INTEGER PRIMARY KEY,
    name TEXT
);

CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    amount REAL,
    date TEXT,
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);

INSERT INTO customers (name) VALUES ('John'), ('Sara'), ('Amit');
INSERT INTO orders (customer_id, amount, date) VALUES
(1, 500, '2023-01-01'),
(1, 300, '2023-01-02'),
(2, 700, '2023-02-01');
""")

conn.commit()
conn.close()

print("✅ Database created successfully!")
