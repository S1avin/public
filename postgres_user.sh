#!/bin/bash

# Check if both username and password are provided
if [ $# -ne 2 ]; then
    echo "Usage: $0 <username> <password>"
    exit 1
fi

username=$1
password=$2

# Execute SQL commands using psql
sudo -u postgres psql << EOF
CREATE USER $username WITH PASSWORD '$password';
GRANT CONNECT ON DATABASE important TO $username;
ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA data
   GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO $username;
EOF

echo "User '$username' provisioned successfully."
