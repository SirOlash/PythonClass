from abc import ABC, abstractmethod

class Logger(ABC):

    @abstractmethod
    def log(self, message,level):
        ...
        # print(f"Message: {message} level: {level}")

    @staticmethod
    def info(self,message,level):
        print(message)

class FileLogger(Logger):
    def log(self, message,level):
        print(f"File: {message} level: {level}")

class DatabaseLogger(Logger):
    def log(self, message,level):
        print(f"Logging into Database: {message} level: {level}")