from constants import Constants
from colorama import Fore

import json
import os


class ConfigParser:
    def __init__(self) -> None:
        self.data = self.loadConfig()

    def loadConfig(self):
        try:
            if os.path.exists(Constants.configPath):
                with open(Constants.configPath, "r") as file: 
                    data = json.load(file)
                    print(Fore.LIGHTGREEN_EX + "[Server] " + Fore.LIGHTMAGENTA_EX + "successfully loaded config")
                    return data
            else:
                with open(Constants.configPath, "w") as file: 
                    json.dump(Constants.configDefault, file, indent=4)
                    print(Fore.LIGHTGREEN_EX + "[Server] " + "Config not found. Generating new config")
                    return Constants.configDefault
        except Exception as e:
            print(Fore.RED + "[CRITICAL] Something went wrong while loading config. If issue cannot be resolved, delete config located at /program/config/devices.json")
            quit()

    def addEntity():
        pass
 
    def popEntity():
        pass

    def addActionGroup():
        pass

    def popActionGroup():
        pass
