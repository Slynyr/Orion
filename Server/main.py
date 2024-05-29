from rest import Rest
from constants import Constants
from homeAssistant import HomeAssistant
from utility import Utility

utility = Utility()
homeAssistant = HomeAssistant()

utility.clearScreen()
utility.printLogo()
utility.printBar()
homeAssistant.pingHomeAssistant()
restApp = Rest()
