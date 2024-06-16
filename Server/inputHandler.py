class InputHandler:
    def __init__(self, configParser, args) -> None:
        self.args = args
        self.configParser = configParser

    def createGroup(self):
        if (self.args.groupName):
            self.configParser.createActionGroup(self.args.groupName)
        else: 
            pass
        quit()

    def addDeviceToGroup(self):
        if (self.args.groupName and self.args.deviceName):
            self.configParser.addDeviceToGroup(self.args.groupName, self.args.deviceName)
        quit()

    def removeDeviceFromGroup(self):
        if (self.args.groupName and self.args.deviceName):
            self.configParser.removeDeviceFromGroup(self.args.groupName, self.args.deviceName)
        quit()

    def addDevice(self):
        if (self.args.deviceName and self.args.entityID):
            self.configParser.addDevice(self.args.deviceName, self.args.entityID)
        quit()

    def removeDevice(self):
        if (self.args.deviceName):
            self.configParser.removeDevice(self.args.deviceName)
        quit()

    def removeGroup(self):
        if (self.args.groupName):
            self.configParser.removeGroup(self.args.groupName)
        quit()

    def isActionCommand(self):
        return (self.args.creategroup or self.args.removeGroup or self.args.addDeviceToGroup or self.args.removeDeviceFromGroup or self.args.addDevice or self.args.removeDevice)