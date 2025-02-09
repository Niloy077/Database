import sqlite3

# Connect to the database
conn = sqlite3.connect('etl_database.db')
cursor = conn.cursor()

# Delete all data from all tables (adjust the table names as needed)
cursor.execute('DELETE FROM customers')  # Replace 'customers' with your actual table name

# Commit and close the connection
conn.commit()
conn.close()