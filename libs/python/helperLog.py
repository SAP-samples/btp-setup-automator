from datetime import datetime
import os

class logtype:
    # Taken from https://stackabuse.com/how-to-print-colored-text-in-python/
    HEADER = "\033[38;5;15m"
    ERROR = "\033[38;5;160m"
    CHECK = "\033[38;5;8m"
    INFO = "\033[38;5;241m"
    COMMAND = "\033[38;5;75m"
    SUCCESS = "\033[38;5;40m"
    WARNING = "\033[38;5;11m"
    USERINPUT = "\033[38;5;51m"

class LOGFILE:
    def __init__(self, btpUsecase):
        self.logfile = btpUsecase.logfile
        createNewEmptyFile(btpUsecase.logfile)
        createNewEmptyFile(btpUsecase.metadatafile)

    def write(self, format, message):

        thisTimestamp = "[" + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "]"
        resetColorCoding = "\033[0;0m"

        if format == logtype.HEADER:
            message = "\n" + "#"*100 +  "\n# " + message.upper() + "\n" + "#"*100
        if format == logtype.ERROR:
            message = "ERROR: " + message
        if format == logtype.CHECK:
            message = "CHECK: " + message
        if format == logtype.COMMAND:
            message = "RUN COMMAND: " + message
        if format == logtype.INFO:
            message = "INFO: " + message
        if format == logtype.SUCCESS:
            message = "SUCCESS: " +  message
        if format == logtype.WARNING:
            message = "WARNING: " + message
        print(logtype.INFO + thisTimestamp + " " + format + message + resetColorCoding)

        with open(self.logfile, "a+") as file_object:
            file_object.write( thisTimestamp + " " + message + "\n")

        return None

def createNewEmptyFile(logfile):
    # Create new log file
    os.makedirs(os.path.dirname(logfile), exist_ok=True)
    if os.path.exists(logfile):
        os.remove(logfile)
    f = open(logfile, "a+")
    f.close
