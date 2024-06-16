from flask import Flask
from colorama import Fore

class Rest:
    def __init__(self, configParser, homeAssistant):
        self.configParser = configParser
        self.homeAssistant = homeAssistant
        self.app = Flask(__name__)    
        self.generateDeviceEndpoints()
        self.generateGroupEndpoints()
        self.app.run(host="0.0.0.0", port=4586, debug=False)

    def generateDeviceEndpoints(self):
        devices = self.configParser.getAllDevices()

        for device in devices:
            self.addDeviceEndpoints(device)
    
    def generateGroupEndpoints(self):
        groups = self.configParser.getAllGroups()

        for group in groups:
            self.addGroupEndpoints(group)
        

    def addDeviceEndpoints(self, device):
        
        def triggerOn():
            print(Fore.LIGHTGREEN_EX + f"{device[0]} was turned on")
            self.homeAssistant.triggerDevice(device[1], "turn_on")
            return f"{device[0]} was triggered"
        
        def triggerOff():
            print(Fore.LIGHTGREEN_EX + f"{device[0]} was turned off")
            self.homeAssistant.triggerDevice(device[1], "turn_off")
            return f"{device[0]} was triggered"
        
        def triggerToggle():
            print(Fore.LIGHTGREEN_EX + f"{device[0]} was toggled")
            self.homeAssistant.triggerDevice(device[1], "toggle")
            return f"{device[0]} was triggered"
        
        self.app.add_url_rule(f'/device/{device[0].replace(" ", "")}/on', f'/device/{device[0].replace(" ", "")}/on', triggerOn, methods=['GET'])
        self.app.add_url_rule(f'/device/{device[0].replace(" ", "")}/off', f'/device/{device[0].replace(" ", "")}/off', triggerOff, methods=['GET'])
        self.app.add_url_rule(f'/device/{device[0].replace(" ", "")}/toggle', f'/device/{device[0].replace(" ", "")}/toggle', triggerToggle, methods=['GET'])

    def addGroupEndpoints(self, group):
        
        def triggerOn():
            print(Fore.LIGHTGREEN_EX + f"{group} was turned on")
            self.homeAssistant.triggerGroup(group, "turn_on")
            return f"{group} was triggered"
        
        def triggerOff():
            print(Fore.LIGHTGREEN_EX + f"{group} was turned off")
            self.homeAssistant.triggerGroup(group, "turn_off")
            return f"{group} was triggered"
        
        def triggerToggle():
            print(Fore.LIGHTGREEN_EX + f"{group} was toggled")
            self.homeAssistant.triggerGroup(group, "toggle")
            return f"{group} was triggered"
        
        self.app.add_url_rule(f'/group/{group.replace(" ", "")}/on', f'/group/{group.replace(" ", "")}/on', triggerOn, methods=['GET'])
        self.app.add_url_rule(f'/group/{group.replace(" ", "")}/off', f'/group/{group.replace(" ", "")}/off', triggerOff, methods=['GET'])
        self.app.add_url_rule(f'/group/{group.replace(" ", "")}/toggle', f'/group/{group.replace(" ", "")}/toggle', triggerToggle, methods=['GET'])