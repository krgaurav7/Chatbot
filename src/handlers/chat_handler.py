from src.agents.chat_agent.graph import create_chat_agent_graph_builder
from langchain.messages import HumanMessage
from src.agents.chat_agent.states.chat_agent_state import ChatAgentState

graph = create_chat_agent_graph_builder()

def chat_agent_handler(message : str) -> ChatAgentState:
   """
   Docstring for chat_agent_handler
   
   :param message: Description
   :type message: str
   :return: Description
   :rtype: dict[str, str]
   """
   return graph.invoke({"messages" : [HumanMessage(content = message)]}) # Note: 'graph' needs to be defined elsewhere and should represent the compiled state graph for the chat agent.
