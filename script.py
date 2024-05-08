import pandas as pd
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('asset_owners.db')
c = conn.cursor()

# Read the large Excel file
hosts_df = pd.read_excel('large_hosts.xlsx')

# Join with the asset_owners table and populate the new column
hosts_df['asset owner'] = hosts_df['hostname'].map(pd.Series(c.execute('''
    SELECT owner FROM asset_owners WHERE hostname = ?'''),
    index=hosts_df['hostname']))

# Fill NaN values with an empty string
hosts_df['asset owner'] = hosts_df['asset owner'].fillna('')

# Reorder the columns to place "asset owner" next to "hostname"
column_order = hosts_df.columns.tolist()
new_column_order = [column_order[0]] + ['asset owner'] + column_order[1:]
hosts_df = hosts_df[new_column_order]

# Save the updated DataFrame back to Excel
hosts_df.to_excel('hosts_with_owners.xlsx', index=False)

# Close the database connection
conn.close()