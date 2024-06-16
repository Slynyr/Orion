from .rest import Rest
from .constants import Constants
from .homeAssistant import HomeAssistant
from .utility import Utility
from .configParser import ConfigParser
from .argsHandler import ArgsHandler
from .inputHandler import InputHandler

def mainEntryPoint():
    args = ArgsHandler.getArgs() 
    utility = Utility()

    #Drawing CLI splash screen
    if not (args.creategroup or args.removeGroup or args.addDeviceToGroup or args.removeDeviceFromGroup or args.addDevice or args.removeDevice or args.listDevices):
        utility.clearScreen()
        utility.printLogo()
        utility.printBar()

    #TODO ADD DEBUG PREFIX
    configParser = ConfigParser(args)
    inputHandler = InputHandler(configParser, args)
    homeAssistant = HomeAssistant(configParser)

    if args.adopt:
        homeAssistant.adoptDevices()
        quit()
    elif args.creategroup:
        inputHandler.createGroup()
    elif args.addDeviceToGroup:
        inputHandler.addDeviceToGroup()
    elif args.removeDeviceFromGroup:
        inputHandler.removeDeviceFromGroup()
    elif args.addDevice:
        inputHandler.addDevice()
    elif args.removeDevice:
        inputHandler.removeDevice()
    elif args.removeGroup: 
        inputHandler.removeGroup()
    elif args.showCWD:
        inputHandler.showCWD()
    elif args.listDevices:
        inputHandler.listDevices()

    homeAssistant.pingHomeAssistant()
    restApp = Rest(configParser, homeAssistant)

if __name__ == "__main__":
    mainEntryPoint()   
