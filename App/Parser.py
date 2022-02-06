import operator

from cv2 import dnn_DetectionModel
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
                        self.dailyCommands += [(minute, hour, dom, month, dow, cmd)]
                    elif (dom, month) == ("*", "*"):
                        self.weeklyCommands += [(minute, hour, dom, month, dow, cmd)]
                    elif (dom) == ("*"):
                        self.monthlyCommands += [(minute, hour, dom, month, dow, cmd)]
                except ValueError:
                    continue  # skip invalid syntax

    @staticmethod
    def _sortByTime(cronItems):
        ''' sort by min, sort by hour '''
        sortedList = sorted(cronItems, key=operator.itemgetter(0), reverse=False)
        sortedList = sorted(sortedList, key=operator.itemgetter(1), reverse=False) 
        return sortedList

    @staticmethod
    def _handleEveryNMin(cronItems):
        return cronItems

    @staticmethod
    def _handleEveryNHour(cronItems):
        return cronItems

    @staticmethod
    def _handleCommaListMin(cronItems):
        logger.debug(cronItems)
        cronItemsNew = []
        for item in cronItems:
            minute = item[0]
            if "," in minute:
                minutes = minute.split(",")
                for min in minutes:
                    cronItemsNew += [(min, item[1:])]
            else:
                cronItemsNew += item
        return cronItemsNew

    @staticmethod
    def _handleCommaListHour(cronItems):
        return cronItems

    def parseDailySchedule(self):
        # self.dailyCommands = Parser._handleEveryNMin(self.dailyCommands)
        # self.dailyCommands = Parser._handleEveryNHour(self.dailyCommands)
        self.dailyCommands = Parser._handleCommaListMin(self.dailyCommands)
        # self.dailyCommands = Parser._handleCommaListHour(self.dailyCommands)
        self.dailyCommands = Parser._sortByTime(self.dailyCommands)
        logger.info(self.dailyCommands)
        self.writer.save()

    def parseWeeklySchedule(self):
        self.weeklyCommands = Parser._sortByTime(self.weeklyCommands)
        logger.info(self.weeklyCommands)
        self.writer.save()

    def parseMonthlySchedule(self):
        self.monthlyCommands = Parser._sortByTime(self.monthlyCommands)
        logger.info(self.monthlyCommands)
        self.writer.save()