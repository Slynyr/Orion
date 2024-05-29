from constants import Constants
import os
from colorama import Fore

class Utility:
    def __init__(self) -> None:
        self.size = os.get_terminal_size()

    def clearScreen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def printBar(self):
        print(Fore.LIGHTMAGENTA_EX + "="*self.size.columns)

    def printLogo(self):
        if (self.size.columns >= 138):
            print(Fore.MAGENTA + Constants.logo)