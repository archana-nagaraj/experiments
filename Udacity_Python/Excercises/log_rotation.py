import logging
import logging.handlers

#Get logger instance
logger = logging.getLogger()
#Set logLevel
logger.setLevel(logging.debug)
#Get handler
handler = logging.handlers.RotatingFileHandler(testlog.log, maxBytes=20, backupCount=6)
#Add handler
logger.addHandler(handler)
for i in range(0,10):
    logger.debug("This is a log file for testing purpose")



