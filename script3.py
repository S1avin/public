import sqlite3
import yaml

# Open the targets.yml file
with open('targets.yml', 'r') as file:
    targets = yaml.safe_load(file)

# Connect to SQLite database
conn = sqlite3.connect('asset_owners.db')
c = conn.cursor()

# Create a table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS asset_owners
             (hostname TEXT PRIMARY KEY, owner TEXT)''')

# Iterate through the targets and insert data into the table
for target_group in targets:
    for target in target_group['targets']:
        hostname = target.split(':')[0]
        owner = target_group['labels']['owner']
        c.execute("INSERT OR REPLACE INTO asset_owners VALUES (?, ?)", (hostname, owner))

# Commit the changes and close the connection
conn.commit()
conn.close()
