from constants import Constants
from colorama import Fore
import requests

class HomeAssistant: 
    headers = {
    "Authorization": f"Bearer {Constants.API_TOKEN}",
    "Content-Type": "application/json",
    }


    def __init__(self, configParse):
        self.configParser = configParse

    def pingHomeAssistant(self):
        try: 
            print(Fore.LIGHTYELLOW_EX + "[Working] " + Fore.LIGHTMAGENTA_EX + "Searching for local Home Assistant instance", end="", flush=True)
            response = requests.get(Constants.HOME_ASSISTANT_URL)

            if (response.status_code == 200):
                print("\r" + Fore.LIGHTGREEN_EX + "[Server] " + Fore.LIGHTMAGENTA_EX + "Home Assistant instance found on local network")
            else:
                print("\r" + Fore.LIGHTYELLOW_EX + f"[WARN] " + Fore.LIGHTMAGENTA_EX + "Home Assistant responded with code {response.status_code}. Some functionality may not be available")
        except Exception as e: 
            print("\r" + Fore.RED + "[WARN] " + Fore.LIGHTMAGENTA_EX + "Failed to reach Home Assistant on initialization")

    def adoptDevices(self):
        print(Fore.LIGHTYELLOW_EX + "[Working] " + Fore.LIGHTMAGENTA_EX + "Adopting devices. This may take a moment", end="", flush=True)

        data = self.getDevices()
        deviceCount = 0

        if data:
            for entry in data: 
                name = entry['attributes'].get('friendly_name', 'No name')
                entityID = entry['entity_id']

                #ignoring entity if not of type light
                if entityID.split(".")[0] != "light":
                    continue
                
                self.configParser.addDevice(name, entityID)
                deviceCount += 1

        print("\r" + Fore.LIGHTGREEN_EX + "[Orion] " + Fore.LIGHTMAGENTA_EX + f"{deviceCount} have been found and adopted                       ")

        print(self.configParser.getAllDevices())

    def getDevices(self):
        url = f"{Constants.HOME_ASSISTANT_URL}/api/states"

        response = requests.get(url=url, headers=self.headers)

        if response.status_code == 200: 
            return response.json()
        else:
            print(f"[WARN] Unable to retrieve devices from home assistant")
            return None
    
    def triggerDevice(self, entityID, action):
        if action not in ["turn_on", "turn_off", "toggle"]:
            print(Fore.RED + f"[ERROR] Invalid action '{action}' for entity {entityID}")
            return
        
        url = f"{Constants.HOME_ASSISTANT_URL}/api/services/light/{action}"
        payload = {"entity_id": entityID}

        try:
            response = requests.post(url, headers=self.headers, json=payload)

            if response.status_code not in [200, 201]:
                print(Fore.RED + f"[ERROR] Failed to send {action} command to {entityID}. HTTP {response.status_code}")
        except:
            print(Fore.RED + f"[ERROR] Failed to send {action} command to {entityID}")

    def triggerGroup(self, group, action):
        if action not in ["turn_on", "turn_off", "toggle"]:
            print(Fore.RED + f"[ERROR] Invalid action '{action}' for group {group}")
            return
        
        groupMembers = self.configParser.getGroupMembers(group)

        for member in groupMembers:
            self.triggerDevice(member[1], action)
        
        