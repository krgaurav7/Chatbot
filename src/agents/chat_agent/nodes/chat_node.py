from langchain_groq import ChatGroq
from src.agents.chat_agent.states.chat_agent_state import ChatAgentState
from dotenv import load_dotenv
from src.agents.chat_agent.tools.date_time import get_current_date_time
from src.agents.chat_agent.tools.web_search import search_the_web
import os

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def chat(state : ChatAgentState) -> ChatAgentState:

    model = ChatGroq(
        model = "openai/gpt-oss-120b",
        api_key=GROQ_API_KEY
    )

    model = model.bind_tools([
        get_current_date_time,
        search_the_web
    ])

    answer = model.invoke(state["messages"])

    return {"messages" : [answer]}