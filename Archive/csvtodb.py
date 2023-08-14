import pandas as pd
import sqlite3

# Load the CSV into a pandas DataFrame
csv_file = 'bigtech.csv'
df = pd.read_csv(csv_file, encoding='ISO-8859-1')

# Ensure the column names match what you've provided
expected_columns = ['Ticker', 'Name', 'Sector', 'Industry', 'Segments', 'Products',
                    'Management', 'Analyst']

if list(df.columns) != expected_columns:
    raise ValueError(
        f"CSV columns do not match expected columns. Found: {df.columns}")

# Connect to SQLite and create a new database
db_file = 'bigtechsev.db'
conn = sqlite3.connect(db_file)

# Convert the DataFrame to SQLite
table_name = 'bigtechsev'
df.to_sql(table_name, conn, if_exists='replace', index=False)

# Close the connection
conn.close()

print(f"CSV data has been imported to {db_file} in table '{table_name}'")
