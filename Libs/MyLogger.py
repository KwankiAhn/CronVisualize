import logging


class MyLogger:
    @staticmethod
    def getLogger(name, level=logging.DEBUG):
        logger = logging.getLogger(name)
        formatter = logging.Formatter('[%(asctime)s][%(levelname)s|%(filename)s:%(lineno)s] >> %(message)s')
        streamHandler = logging.StreamHandler()
        streamHandler.setFormatter(formatter)
        logger.addHandler(streamHandler)

        # fileHandler = logging.FileHandler('./test.log')
        # fileHandler.setFormatter(formatter)
        # self.logger.addHandler(fileHandler)

        logger.setLevel(level=level)
        return logger
