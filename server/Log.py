from datetime import datetime

class Log:


    def __init__(self, message, logType):

        timestamp = datetime.now().strftime("%d-%m-%YT%H:%M:%S")  # get timestand


        with open("chat_history.log", "a") as f:
            f.write("{}: {} - {}\n".format(logType,timestamp, message))
            f.close
        

class LogType: 
    ERROR = "Error"
    WARNING = "Warning"
    DEBUG = "Debug Mode"