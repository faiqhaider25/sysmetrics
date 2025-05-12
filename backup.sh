#!/bin/bash

# Set backup directory with date
BACKUP_DIR="backup_$(date +%Y-%m-%d_%H-%M-%S)"

# Create backup directory
mkdir "$BACKUP_DIR"

# Copy docker-compose and src folder
cp docker-compose.yml "$BACKUP_DIR"/
cp -r src/ "$BACKUP_DIR"/

echo "Backup created"

