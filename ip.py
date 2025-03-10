import os
import time
import json
import urllib.request
import colorama
from colorama import Fore, Style

colorama.init()

ENV_FILE = ".env"

API_LIMIT_URL = "https://api.ipfind.com/me?auth={api_key}"
IP_LOOKUP_URL = "https://api.ipfind.com?ip={ip}&auth={api_key}"

def read_api_key():
    if not os.path.exists(ENV_FILE):
        return None

    with open(ENV_FILE, "r") as file:
        for line in file:
            if line.startswith("API="):
                return line.strip().split("=")[1]
    return None

def write_api_key(api_key):
    with open(ENV_FILE, "w") as file:
        file.write(f"API={api_key}")

def check_api_limit(api_key):
    try:
        url = API_LIMIT_URL.format(api_key=api_key)
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())

        if "error" in data:
            return False
        return True
    except Exception:
        return False

def fetch_ip_info(ip_address, api_key):
    try:
        url = IP_LOOKUP_URL.format(ip=ip_address, api_key=api_key)
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())

        if "error" in data:
            print(Fore.RED + "Error: Invalid IP or API key issue." + Style.RESET_ALL)
            return

        print(Fore.GREEN + "\nIP Address Details:" + Style.RESET_ALL)
        print(Fore.CYAN + f"IP Address: {data.get('ip_address', 'N/A')}")
        print(f"Country: {data.get('country', 'N/A')} ({data.get('country_code', 'N/A')})")
        print(f"City: {data.get('city', 'N/A')}")
        print(f"Region: {data.get('region', 'N/A')} ({data.get('region_code', 'N/A')})")
        print(f"Continent: {data.get('continent', 'N/A')} ({data.get('continent_code', 'N/A')})")
        print(f"Timezone: {data.get('timezone', 'N/A')}")
        print(f"Latitude: {data.get('latitude', 'N/A')}")
        print(f"Longitude: {data.get('longitude', 'N/A')}")
        print(f"Currency: {data.get('currency', 'N/A')}")
        print(f"Languages: {', '.join(data.get('languages', []))}" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"Error fetching IP details: {e}" + Style.RESET_ALL)

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

api_key = read_api_key()

if api_key:
    if check_api_limit(api_key):
        clear_screen()
        ip_address = input("Enter IP Address: ").strip()
        fetch_ip_info(ip_address, api_key)
    else:
        print(Fore.RED + "API limit reached or invalid key. Please check your account." + Style.RESET_ALL)
else:
    print(Fore.WHITE + "Please create an account" + Style.RESET_ALL)
    print(Fore.BLUE + "https://ipfind.com/signup" + Style.RESET_ALL)
    time.sleep(10)

    print("\nMust confirm your email to activate your API key.")
    print("Must check and confirm your API before using this tool.")
    time.sleep(20)

    api_key = input("\nEnter your API KEY: ").strip()

    write_api_key(api_key)

    clear_screen()
    ip_address = input("Enter IP Address: ").strip()
    fetch_ip_info(ip_address, api_key)
