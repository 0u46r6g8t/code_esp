import json
from logging import warning
from datetime import datetime
import time
from typing import List

class Debugger():
    PATH_LOG = "logs/"
    PATH_JSON = "json/"
        
    __fileLog = "debug.log"
    __errorLog = "error.log"
    __jsonLog = "jsonResponse.json"    

    __error: dict = None

    def __init__(self, _active=False) -> None:
        self.__error = None
        self.__active = _active
        self.__fileLog = self.PATH_LOG + self.__fileLog
        self.__errorLog = self.PATH_LOG + self.__errorLog
        self.__jsonLog = self.PATH_LOG + "jsonResponse.json"
        
    def setDebug(self, _active: bool) -> None:
        self.__active = _active
    
    def log(self, _msg:str):
        if(self.__active):        
            warning(f"[DEBUG]: {_msg}")
    
    def __mountLog(
        self,
        _logMessage: str = None,
        _type: str = None,
        _statusCode=None,
    ):
        dateNow = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        return f"[{_type} -> {_statusCode} ] - {dateNow}: {_logMessage}\n"

    def __write(self, message:str, nameFile:str, mode:str = "a+"):
        
        with open(nameFile, mode) as file:
            file.write(message)

        file.close()
        

    def writeLog(
        self, _logMessage: str = None, _statusCode=None, _jsonLog: str = None
    ):
        message = self.__mountLog(_logMessage, "LOG", _statusCode)

        self.__write(message, self.__fileLog)
        
        self.__write(json.dumps(_jsonLog, indent=4), self.__jsonLog, "w+")

    def writeError(self, _errorMessage: str = None, _statusCode=None):
        message = self.__mountLog(_errorMessage, "ERROR", _statusCode)

        self.__write(message, self.__errorLog)

    def saveError(self, _error: str, _message: str) -> None:
        self.__error = {'typeError': _error, 'message': _message}

        self.writeError(_error)

    def getError(self):
        if (self.__error is None):
            return {
                'typeError': None,
                'message': None
            }
            
        return self.__error
    
    def startTimmer(self):
        self.__startTimmer = time.time()

    def checkoutTimmer(self, _nameFunction:str):
        timer = time.time() - self.__startTimmer

        self.log(f"[{_nameFunction}]: {timer}")