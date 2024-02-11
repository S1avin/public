import pandas as pd
import sqlite3

# Load the Excel file
df_excel = pd.read_excel("file.xlsx")

# Connect to the SQLite database
conn = sqlite3.connect("db.db")

# Query to retrieve Hostname and Owner from the database
query = "SELECT Hostname, Owner FROM table1"

# Execute the query and fetch all rows
cursor = conn.cursor()
cursor.execute(query)
rows = cursor.fetchall()

# Create a dictionary to map Hostname to Owner
hostname_to_owner = {hostname: owner for hostname, owner in rows}

# Add a new column 'Owner' to the DataFrame and populate it
df_excel['Owner'] = df_excel['Hostname'].map(hostname_to_owner)

# Save the modified DataFrame back to Excel
df_excel.to_excel("modified_file.xlsx", index=False)

# Close the database connection
conn.close()
