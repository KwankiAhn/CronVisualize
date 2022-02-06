
from App.Parser import Parser
from App.ImageWriter import ImageWriter
from Libs.MyLogger import MyLogger
from Libs.ArgParser import ArgParserBase

logger = MyLogger.getLogger(__name__)


if __name__ == "__main__":   
    logger.info("d/app start...")

    argParser = ArgParserBase()
    argParser.parseArgs()
    argParser.printArgs()

    writer = ImageWriter()

    cronParser = Parser(argParser.cronInput, writer)
    cronParser.parseDailySchedule()
    cronParser.parseWeeklySchedule()
    cronParser.parseMonthlySchedule()
