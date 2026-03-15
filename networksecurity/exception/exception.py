import sys              # Provides information about the Python runtime environment like file name, line number, traceback
from networksecurity.logging import logger
class NetworkSecurityException(Exception):          # creating a custom exception class inherit from Python’s built-in Exception class.
    def __init__(self, error_message, error_details: sys):      # error_message: the original error message. error_details: system error info (sys)
        self.error_message = error_message                  
        _,_,exc_tb = error_details.exc_info()               # This line extracts exception information. exc_tb -> traceback: where exception occured.

        self.lineno = exc_tb.tb_lineno                              # traceback line number
        self.file_name = exc_tb.tb_frame.f_code.co_filename         # This extracts the file where the error occurred
    
    def __str__(self):                      # defines how the error message will be printed.
        return "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(self.file_name, self.lineno, str(self.error_message))