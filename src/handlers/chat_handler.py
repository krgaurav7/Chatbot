from src.agents.chat_agent.graph import create_chat_agent_graph_builder
from langchain.messages import HumanMessage
from src.agents.chat_agent.states.chat_agent_state import ChatAgentState

graph = create_chat_agent_graph_builder()

def chat_agent_handler(thread_id : str , message : str) -> ChatAgentState:
   """
   Docstring for chat_agent_handler
   
   :param message: Description
   :type message: str
   :return: Description
   :rtype: dict[str, str]
   """
   return graph.invoke(
      input = {
         "messages" : [HumanMessage(content = message)]
               },
               config={
                  "configurable" : {
                     "thread_id" : [thread_id]
                  }
               }
      ) # Note: 'graph' needs to be defined elsewhere and should represent the compiled state graph for the chat agent.

def get_all_threads_handler():
   """
   Docstring for get_all_threads_handler
   """
   all_checkpoints = graph.checkpointer.list(config = {})

   threads = set()

   for checkpoint in all_checkpoints:
      threads.add(checkpoint.config["configurable"]["thread_id"])
   return list(threads)

def chat_history_handler(thread_id : str) :
   """
   Docstring for chat_history_handler
   """
   return graph.get_state(config = {
      "configurable" : {
         "thread_id" : [thread_id]
      }
   })[0]  #or we use ["channel_values"]