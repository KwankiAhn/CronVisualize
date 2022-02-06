from Libs.MyLogger import MyLogger

logger = MyLogger.getLogger(__name__)


class Parser:
    def __init__(self, scheduleFilename, writer):
        logger.info(f"parser init w/ {scheduleFilename}")
        self.writer = writer
        self.scheduleFilename = scheduleFilename
        self.dailyCommands = []
        self.weeklyCommands = []
        self.monthlyCommands = []
        self._readParseFile()

    def _readParseFile(self):
        with open(self.scheduleFilename, "r") as scheduleContent:
            lines = scheduleContent.readlines()
            for line in lines:
                line = line.strip()  # remove carrage return
                try:
                    if line.startswith("#"):
                        continue
                    minute, hour, dom, month, dow, cmd = line.split(" ")
                    logger.info((minute, hour, dom, month, dow, cmd))
                    if (dom, month, dow) == ("*", "*", "*"):
                        self.dailyCommands += (minute, hour, dom, month, dow, cmd)
                    elif (dom, month) == ("*", "*"):
                        self.weeklyCommands += (minute, hour, dom, month, dow, cmd)
                    elif (dom) == ("*"):
                        self.monthlyCommands += (minute, hour, dom, month, dow, cmd)
                except ValueError:
                    continue  # skip invalid syntax

    def parseDailySchedule(self):
        logger.info(self.dailyCommands)
        self.writer.save()

    def parseWeeklySchedule(self):
        logger.info(self.weeklyCommands)
        self.writer.save()

    def parseMonthlySchedule(self):
        logger.info(self.monthlyCommands)
        self.writer.save()