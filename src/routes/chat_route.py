from fastapi import APIRouter
from src.handlers.chat_handler import chat_agent_handler
from src.agents.chat_agent.states.chat_agent_state import ChatAgentState
from src.handlers.chat_handler import get_all_threads_handler, chat_history_handler, chat_streaming_handler
from fastapi.responses import StreamingResponse

router = APIRouter()

@router.post("/chat/{thread_id}")
def chat_agent_route(thread_id: str, message : str) -> ChatAgentState:
    """
    Docstring for chat_agent_route
    
    :param message: Description
    :type message: str
    :return: Description
    :rtype: ChatAgentState
    """
    return chat_agent_handler(thread_id = thread_id, message = message )

@router.post("/stream/{thread_id}")
def chat_stream_route(thread_id : str, message : str):
    """
    Docstring for chat_stream_route
    
    :param thread_id: Description
    :type thread_id: str
    :param message: Description
    :type message: str
    """
    return StreamingResponse(
        chat_streaming_handler( thread_id , message ),
        media_type="text/plain"
    )

@router.get("/chat/threads")
def get_all_threads() -> list[str | None]:
    """
    Docstring for get_all_threads
    """
    return get_all_threads_handler()

@router.get("/chat/history/{thread_id}")
def get_chat_history(thread_id : str) -> ChatAgentState | dict[None , None]:
    """
    Docstring for get_chat_history
    """
    return chat_history_handler(thread_id = thread_id)