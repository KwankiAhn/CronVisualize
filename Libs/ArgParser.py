import argparse
from Libs.MyLogger import MyLogger

logger = MyLogger.getLogger(__name__)


class ArgParserBase:
    def __init__(self, desc=None):
        self.argParser = argparse.ArgumentParser(description=desc)
        self.argParser.add_argument("--cronInput", help="cron schedule definition filename")

    def parseArgs(self):
        args, _ = self.argParser.parse_known_args()
        self.cronInput = args.cronInput
    
    def printArgs(self):
        for key, val in self.__dict__.items():
            if key != "argParser":
                logger.info("{}: {}".format(key, val))