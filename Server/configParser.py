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
                data = {"devices": [], "groups": []}
                with open(Constants.configPath, "w") as file: 
                    json.dump(data, file, indent=4)
                    print(Fore.LIGHTGREEN_EX + "[Server] " + Fore.LIGHTMAGENTA_EX + "Config not found. Generating new config")
                    return data
        except Exception as e:
            print(Fore.RED + "[CRITICAL] Something went wrong while loading config. If issue cannot be resolved, delete config located at /program/config/devices.json")
            if (self.args.debug):
                print(e)

            quit()

    # DEVICE 
    def addDevice(self, name, entityID):
        if not any(device for device in self.data['devices'] if device["name"] == name): # making sure device is not already added
            device = {"name": name, "entityID": entityID}
            self.data['devices'].append(device)
            self.saveConfig()

    def popEntity():
        pass

    def getAllDevices(self):
        devices = []

        for device in self.data['devices']:
            devices.append([device["name"], device["entityID"]])
        
        return devices
    
    def getDeviceByName(self, name):
        for device in self.data['devices']:
            if device["name"] == name:
                return [device["name"], device["entityID"]]
        return None

    # GROUPS 
    def createActionGroup(self, name):
        print("attempting")
        if not any(group for group in self.data['groups'] if group['name'] == name): # making sure device is not already added
            print("I tried")
            groupJson = {"name": f"{name}", "members": []}
            self.data['groups'].append(groupJson)
            self.saveConfig() 

    def addDeviceToGroup(self, groupName, deviceName):
        if any(group for group in self.data['groups'] if group['name'] == groupName) and any(device for device in self.data['devices'] if device["name"] == deviceName):
            device = self.getDeviceByName(deviceName)

            if not device:
                print(Fore.RED + "[CRITICAL] Something went wrong while adding device to group")
                return None
            
            deviceJson = {"name": device[0], "entityID": device[1]}

            for group in self.data['groups']:
                if group["name"] == groupName:
                    group["members"].append(deviceJson)

            self.saveConfig()

        else: 
            print("No findie") #TODO fix messages

    def removeDeviceFromGroup(self, groupName, deviceName):
        if any(group for group in self.data['groups'] if group['name'] == groupName):
            for group in self.data['groups']:
                if group["name"] == groupName:
                    newMembers = []

                    for member in group["members"]:
                        if member["name"] != deviceName:
                            newMembers.append(member)
                    group["members"] = newMembers
                    break
        
            self.saveConfig()

    def getAllGroups(self):
        groups = []

        for group in self.data['groups']:
            groups.append(group["name"])
        
        return groups
    
    def getGroupMembers(self, groupName):
        members = []

        for group in self.data['groups']:
            if group["name"] == groupName:
                for member in group["members"]:
                    members.append([member["name"], member["entityID"]])
                return members
        return members



    def saveConfig(self):
        try:
            with open(Constants.configPath, "w") as file:
                json.dump(self.data, file, indent=4)
        except Exception as e:
            print(Fore.RED + "[CRITICAL] Something went wrong while saving config.")
            if self.args.debug:
                print(e)
