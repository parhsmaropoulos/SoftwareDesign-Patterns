# Dependency Inversion Principle
# High level modules should not depend upon low level modules. Both should depend upon abstractions.
# Abstractions should not depend on details. Details should depend on abstractions.


# A logger inteface that logs a message
class I_Logger:
    def Log_Message(self, message):
        pass

# A db logger implement the logger interface and log a message.


class DB_Logger(I_Logger):
    def Log_Message(self, message):
        print(message)
        return

# A file logger implement the logger interface and log a message.


class File_Logger(I_Logger):
    def Log_Message(self, stack_trace):
        print(stack_trace)
        return

# A event logger implement the logger interface and log a message.


class Event_Logger(I_Logger):
    def Log_Message(self, message):
        print(message)
        return

# Exception logger class creates an object
# of logger interface


class Exception_Logger:
    __logger = I_Logger()

    # Initialize the object
    def __init__(self, logger):
        self.__logger = logger
        return
    # Logs the exception depending the type of logger class

    # Convert exception text to string
    def __Get_User_Readable_Message(self, exception):
        message = "made humanable"
        # convert ex to nomal format
        return message

    def Log_Exception(self, exception):
        self.__logger.Log_Message(self.__Get_User_Readable_Message(exception))
        return


# Data explorer class that reads data from a file and depending on the error
# it creates a logger of either 3 classes and log the message
class Data_Exporter:
    def Export_Data_From_File():
        try:
            print("export data")
        except IOError:
            __exception_logger = Exception_Logger(DB_Logger())
            __exception_logger.Log_Exception(IOError)
        except EnvironmentError:
            __exception_logger = Exception_Logger(Event_Logger())
            __exception_logger.Log_Exception(EnvironmentError)
        except:
            __exception_logger = Exception_Logger(File_Logger())
            __exception_logger.Log_Exception("exception heres")
