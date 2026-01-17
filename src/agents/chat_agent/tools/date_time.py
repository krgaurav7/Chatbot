import time
from langchain.tools import tool

@tool
def get_current_date_time() -> str:
    """
    use this tool to get the current date and time
    Docstring for get_current_date_time
    
    :return: Description
    :rtype: str
    """
    return time.ctime()