#!/bin/bash

echo "=== CPU Usage ==="
top -bn1 | grep "Cpu(s)"

echo -e "\n=== Memory Usage ==="
free -h

echo -e "\n=== Disk Usage ==="
df -h

echo -e "\n=== Network Info ==="
ip a
