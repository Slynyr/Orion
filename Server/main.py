from rest import Rest
from constants import Constants
from homeAssistant import HomeAssistant
from utility import Utility
from configParser import ConfigParser

utility = Utility()
homeAssistant = HomeAssistant()

#Drawing CLI splash screen
utility.clearScreen()
utility.printLogo()
utility.printBar()

#TODO ADD DEBUG PREFIX

configParser = ConfigParser()
homeAssistant.pingHomeAssistant()
restApp = Rest()
