from constants import Constants
from colorama import Fore

import json
import os


class ConfigParser:
    def __init__(self, args) -> None:
        self.data = self.loadConfig()
        self.args = args

    def ensureDirExists(self):
        directory = os.path.dirname(Constants.configPath)
        if not os.path.exists(directory):
            os.makedirs(directory)

    def loadConfig(self):
        try:
            self.ensureDirExists()
            if os.path.exists(Constants.configPath):
                with open(Constants.configPath, "r") as file: 
                    data = json.load(file)
                    print(Fore.LIGHTGREEN_EX + "[Server] " + Fore.LIGHTMAGENTA_EX + "successfully loaded config")
                    return data
            else:
                with open(Constants.configPath, "w") as file: 
                    json.dump(Constants.configDefault, file, indent=4)
                    print(Fore.LIGHTGREEN_EX + "[Server] " + Fore.LIGHTMAGENTA_EX + "Config not found. Generating new config")
                    return Constants.configDefault
        except Exception as e:
            print(Fore.RED + "[CRITICAL] Something went wrong while loading config. If issue cannot be resolved, delete config located at /program/config/devices.json")
            if (self.args.debug):
                print(e)

            quit()

    def addEntity():
        pass
 
    def popEntity():
        pass

    def addActionGroup():
        pass

    def popActionGroup():
        pass
