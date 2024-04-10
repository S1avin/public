#!/bin/bash

# Backup settings
SOURCE_DIR="/path/to/your/directory"
BACKUP_DIR="/path/to/your/backup/directory"
DATE=$(date +"%Y-%m-%d")
BACKUP_NAME="backup-$DATE.tar.gz"

# Create a backup
tar -czf $BACKUP_DIR/$BACKUP_NAME $SOURCE_DIR

# Find and delete backups older than 30 days
find $BACKUP_DIR -type f -name "*.tar.gz" -mtime +30 -exec rm {} \;

