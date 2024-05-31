from constants import Constants
from colorama import Fore
import requests

class HomeAssistant: 
    def __init__(self):
        pass

    def pingHomeAssistant(self):
        try: 
            print(Fore.LIGHTYELLOW_EX + "[Working] " + Fore.LIGHTMAGENTA_EX + "Searching for local Home Assistant instance", end="", flush=True)
            response = requests.get(Constants.tempHomeAssistantURL)

            if (response.status_code == 200):
                print("\r" + Fore.LIGHTGREEN_EX + "[Server] " + Fore.LIGHTMAGENTA_EX + "Home Assistant instance found on local network")
            else:
                print("\r" + Fore.LIGHTYELLOW_EX + f"[WARN] " + Fore.LIGHTMAGENTA_EX + "Home Assistant responded with code {response.status_code}. Some functionality may not be available")
        except Exception as e: 
            print("\r" + Fore.RED + "[WARN] " + Fore.LIGHTMAGENTA_EX + "Failed to reach Home Assistant on initialization")