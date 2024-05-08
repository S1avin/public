import pandas as pd

# Read the large Excel file with hostnames
hosts_df = pd.read_excel('kenna_daily.xlsx')

# Read the small Excel file with asset owners
owners_df = pd.read_excel('owners.xlsx', usecols=['Hostname', 'asset_owner'])

# Convert the owners DataFrame to a dictionary for faster lookup
owners_dict = owners_df.set_index('Hostname')['asset_owner'].to_dict()

# Populate the "asset_owner" column using the dictionary
hosts_df['asset_owner'] = hosts_df['Hostname'].map(owners_dict)

# Fill NaN values with an empty string
hosts_df['asset_owner'] = hosts_df['asset_owner'].fillna('')

# Save the updated DataFrame back to Excel
hosts_df.to_excel('kenna_daily_with_owners.xlsx', index=False)