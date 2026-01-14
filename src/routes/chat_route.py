from fastapi import APIRouter
from src.handlers.chat_handler import chat_agent_handler
from src.agents.chat_agent.states.chat_agent_state import ChatAgentState

router = APIRouter()

@router.post("/chat")
def chat_agent_route(message : str) -> ChatAgentState:
    """
    Docstring for chat_agent_route
    
    :param message: Description
    :type message: str
    :return: Description
    :rtype: ChatAgentState
    """
    return chat_agent_handler(message = message)
