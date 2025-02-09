import sqlite3

conn = sqlite3.connect("etl_database.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM customers;")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
