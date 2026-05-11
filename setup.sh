#!/bin/bash

echo -e "\033[1;32m[!] CYBER BOSS ENAFUL System Initializing..."
sleep 2


echo -e "\033[1;34m[*] Installing Dependencies..."
pkg update -y && pkg upgrade -y
pkg install python git termux-api -y


pip install requests

echo -e "\033[1;32m[✔] All Dependencies Installed Successfully!"
sleep 1


if [ -f "Enaful_Locked.py" ]; then
    echo -e "\033[1;36m[🚀] Starting CYBER BOSS ENAFUL V7.0..."
    python Enaful_Locked.py
else
    echo -e "\033[1;31m[!] Main file not found!"
fi
