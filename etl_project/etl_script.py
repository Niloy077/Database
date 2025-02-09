import pandas as pd
import sqlite3

# Database file
DB_FILE = "etl_database.db"

def extract_data(file_path):
    """Extract data from CSV."""
    return pd.read_csv(file_path)

def transform_data(df):
    """Simple data cleaning: drop NaNs and convert names to uppercase."""
    df.dropna(inplace=True)
    df["name"] = df["name"].str.upper()
    return df

def load_data(df, table_name="customers"):
    """Load data into SQLite database."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER PRIMARY KEY, name TEXT, age INT);")

    for _, row in df.iterrows():
        cursor.execute(f"INSERT INTO {table_name} (name, age) VALUES (?, ?)", (row["name"], row["age"]))
    
    conn.commit()
    cursor.close()
    conn.close()

def run_etl():
    df = extract_data("data/customers.csv")
    df = transform_data(df)
    load_data(df)

if __name__ == "__main__":
    run_etl()
