from rest import Rest
from constants import Constants
from homeAssistant import HomeAssistant
from utility import Utility
from configParser import ConfigParser
from argsHandler import ArgsHandler
from inputHandler import InputHandler

args = ArgsHandler.getArgs() 
utility = Utility()

#Drawing CLI splash screen
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

homeAssistant.pingHomeAssistant()
restApp = Rest(configParser, homeAssistant)
