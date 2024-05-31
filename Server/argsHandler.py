import argparse

class ArgsHandler:
    def getArgs():
        parser = argparse.ArgumentParser(description="A Home Assistant Rest API Interface!")
        parser.add_argument("--debug", type=bool, default=False, help="Debug verbose.")
        return parser.parse_args()
