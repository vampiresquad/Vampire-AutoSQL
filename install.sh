#!/bin/bash
echo "[*] Updating packages..."
pkg update -y && pkg upgrade -y
pkg install git python -y
pip install requests termcolor paramspider

echo "[*] Cloning sqlmap..."
git clone https://github.com/sqlmapproject/sqlmap.git

mkdir -p output

echo "[✓] Installation complete. Run with: python3 vampire-autosql.py <site>"
