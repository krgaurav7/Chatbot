import time
from langchain.tools import tool

@tool
def get_current_date_time() -> str:
    """
    Docstring for get_current_date_time
    
    :return: Description
    :rtype: str
    """
    return time.ctime()