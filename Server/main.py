from rest import Rest
from constants import Constants
from homeAssistant import HomeAssistant
from utility import Utility
from configParser import ConfigParser
from argsHandler import ArgsHandler

args = ArgsHandler.getArgs() 
utility = Utility()
homeAssistant = HomeAssistant()

#Drawing CLI splash screen
utility.clearScreen()
utility.printLogo()
utility.printBar()

#TODO ADD DEBUG PREFIX

configParser = ConfigParser(args)
homeAssistant.pingHomeAssistant()
restApp = Rest()
