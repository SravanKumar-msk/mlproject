import sys 

from src.logger import logging


def error_mesasge_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info() # which file, whcih line the exception has occured
    file_name=exc_tb.tb_frame.f_code.co_filename ## it gives the file name error 
    error_message="Error occured in python script name[{0}] line number [{1}] error message [{2}]".format(
    file_name, exc_tb.tb_lineno,str(error))

    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_mesage = error_mesasge_detail(error_message,error_detail=error_detail)

    
    def __str__(self):
        return self.error_mesage
    
if __name__=="__main__":
    try:
        a=1/0
    except Exception as e:
        logging.info("Divide by zero")
        raise CustomException(e,sys)