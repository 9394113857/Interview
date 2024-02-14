import sqlite3
from tabulate import tabulate

# Connect to the SQLite database
conn = sqlite3.connect('database_files/operations.db')
cursor = conn.cursor()

# Retrieve data from the Operations table
cursor.execute("SELECT * FROM Operations")
data = cursor.fetchall()

# Close the database connection
conn.close()

# Add a serial number (SNo) column to the data
data_with_sno = [(i+1,) + row for i, row in enumerate(data)]

# Display the data in a table format
headers = ['SNo', 'Operation', 'Result']
print(tabulate(data_with_sno, headers=headers, tablefmt="grid"))
