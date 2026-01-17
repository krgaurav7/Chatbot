from langchain_community.tools import DuckDuckGoSearchRun
from langchain.tools import tool

search = DuckDuckGoSearchRun()

@tool
def search_the_web(query: str) -> str:
    """
    use this tool to search the web for relevant information
    Docstring for search_the_web
    
    :param query: Description
    :type query: str
    :return: Description
    :rtype: str
    """
    return search.invoke(query)