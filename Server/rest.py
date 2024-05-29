from flask import Flask
from colorama import Fore

class Rest:
    def __init__(self):
        self.app = Flask(__name__)    
        self.setupRoutes()
        self.app.run(host="0.0.0.0", port=4586, debug=False)

    def setupRoutes(self):
        @self.app.route('/button1', methods=['GET'])
        def button1():
            print(Fore.LIGHTMAGENTA_EX + "[Event] Button 1 triggered")
            return "Button1 Triggered", 200

        @self.app.route('/button2', methods=['GET'])
        def button2():  
            print(Fore.LIGHTMAGENTA_EX + "[Event] Button 2 triggered")
            return "Button2 Triggered", 200