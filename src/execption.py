import sys
import logging
def error_message_detail(error,error_details:sys):
    _,_,exc_tb=error_details.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in script [{0}] at line number [{1}] with message [{2}]".format(file_name,exc_tb.tb_lineno,str(error))
    return error_message

'''
✅ Final-Tip

Always call super().__init__() when inheriting from built-in classes like Exception, BaseModel, etc., even if you're storing extra/custom fields. It's a best practice in Python.

'''
class CustomException(Exception):
    def __init__(self,error_message,error_details:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message,error_details=error_details)
    def __str__(self):
        return self.error_message
    

# Entry point
