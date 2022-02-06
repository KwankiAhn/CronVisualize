from Libs.MyLogger import MyLogger

logger = MyLogger.getLogger(__name__)


class Parser:
    def __init__(self, scheduleFilename, writer):
        logger.info(f"parser init w/ {scheduleFilename}")

    def parseDailySchedule(self, saveFormat="png"):
        pass

    def parseWeeklySchedule(self, saveFormat="png"):
        pass

    def parseMonthlySchedule(self, saveFormat="png"):
        pass