#!/bin/bash

clear
echo -e "\e[1;31m"
echo "╔═╗╦  ╦╔╦╗╔═╗╔═╗╦═╗  ╔═╗╔═╗╔═╗╔═╗"
echo "╠═╝║  ║ ║ ║╣ ╠═╣╠╦╝  ║  ╠═╣╠═╝╠═╣"
echo "╩  ╩═╝╩ ╩ ╚═╝╩ ╩╩╚═  ╚═╝╩ ╩╩  ╩ ╩"
echo -e "\e[1;32m        Vampire Squad - Auto Installer"
echo -e "\e[0m"

# Check and update packages
echo "[*] Updating packages..."
pkg update -y && pkg upgrade -y

# Install required packages
echo "[*] Installing dependencies..."
pkg install -y python git curl wget unzip

# Install pip packages
echo "[*] Installing Python modules..."
pip install --upgrade pip
pip install termcolor

# Clone sqlmap if not present
if [ ! -d "sqlmap" ]; then
    echo "[*] Cloning SQLMap..."
    git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git
fi

# Install ParamSpider
if ! command -v paramspider &> /dev/null; then
    echo "[*] Installing ParamSpider..."
    pip install git+https://github.com/devanshbatham/paramspider.git
fi

# Create output directory
mkdir -p output

echo -e "\n\e[1;32m[✔] All done! Run the tool using:\e[0m"
echo -e "\e[1;33mpython3 vampire-autosql.py <url>\e[0m"
