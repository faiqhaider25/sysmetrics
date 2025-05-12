#!/bin/bash

echo "Starting SysPulse container..."
docker-compose down
docker-compose up --build -d
