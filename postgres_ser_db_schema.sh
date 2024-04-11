#!/bin/bash

# Check if all required arguments are provided
if [ $# -ne 5 ]; then
    echo "Usage: $0 <username> <password> <database> <schema>"
    exit 1
fi

username=$1
password=$2
database=$3
schema=$4

# Execute SQL commands using psql
sudo -u postgres psql << EOF
CREATE USER $username WITH PASSWORD '$password';
GRANT CONNECT ON DATABASE $database TO $username;
GRANT USAGE ON SCHEMA $schema TO $username;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA data TO $username;
ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA $schema
   GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO $username;
EOF

echo "User '$username' provisioned successfully."
