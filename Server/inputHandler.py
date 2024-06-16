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

    def removeDeviceFromGroup(self):
        if (self.args.groupName and self.args.deviceName):
            self.configParser.removeDeviceFromGroup(self.args.groupName, self.args.deviceName)