import argparse

class ArgsHandler:
    def getArgs():
        parser = argparse.ArgumentParser(description="A Home Assistant Rest API Interface!")
        parser.add_argument("--debug", action='store_true', help="Debug verbose.")
        parser.add_argument("--adopt", action='store_true', help="Automatically adopts all devices visible on network.")
        parser.add_argument("--creategroup", action='store_true', help="")
        parser.add_argument("--groupName", type=str, default=None , help="")
        parser.add_argument("--addDeviceToGroup", action='store_true', help="")
        parser.add_argument("--deviceName", type=str, default=None , help="")
        parser.add_argument("--entityID", type=str, default=None , help="")
        parser.add_argument("--removeDeviceFromGroup", action='store_true', help="")
        parser.add_argument("--addDevice", action='store_true', help="")
        parser.add_argument("--removeDevice", action='store_true', help="")
        parser.add_argument("--removeGroup", action='store_true', help="")
        parser.add_argument("--showCWD", action='store_true', help="")
        parser.add_argument("--listDevices", action='store_true', help="")

        return parser.parse_args()
