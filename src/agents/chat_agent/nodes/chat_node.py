from langchain_groq import ChatGroq
from src.agents.chat_agent.states.chat_agent_state import ChatAgentState
from dotenv import load_dotenv
from src.agents.chat_agent.tools.date_time import get_current_date_time
import os

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def chat(state : ChatAgentState) -> ChatAgentState:

    model = ChatGroq(
        model = "llama-3.1-8b-instant",
        api_key=GROQ_API_KEY
    )

    model = model.bind_tools([
        get_current_date_time
    ])

    answer = model.invoke(state["messages"])

    return {"messages" : [answer]}