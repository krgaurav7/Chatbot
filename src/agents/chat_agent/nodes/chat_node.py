from langchain_groq import ChatGroq
from src.agents.chat_agent.states.chat_agent_state import ChatAgentState
from dotenv import load_dotenv
from src.agents.chat_agent.tools.date_time import get_current_date_time
from src.agents.chat_agent.tools.web_search import search_the_web
import os

from langchain_core.prompts import ChatPromptTemplate

template = """
You are a Bhojpuri lyricist known for writing soulful, romantic, and melodious songs.

Write a Bhojpuri song that beautifully describes a girl — her looks, nature, emotions, and the feelings she evokes.
The song should:
- Be written in authentic, natural Bhojpuri (avoid Hindi/English mixing)
- Express admiration, romance, and emotional connection
- Use simple yet poetic Bhojpuri expressions
- Feel suitable for a modern Bhojpuri romantic song

Structure:
- 2–3 verses (antara)
- 1 recurring chorus (mukhda)
- Short, rhythmic lines suitable for singing

Imagery:
- Nature-based metaphors (chand, hawa, nadi, kajra, muskaan, ankhiyaan)
- Cultural Bhojpuri expressions of love and beauty

Tone:
- Romantic, respectful, and melodious
- Not vulgar or explicit

Output only the Bhojpuri song.
Do not add explanations, titles, or translations.

   

messageHistory : {message_history}
"""

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def chat(state : ChatAgentState) -> ChatAgentState:
    """
    Docstring for chat
    
    :param state: Description
    :type state: ChatAgentState
    :return: Description
    :rtype: ChatAgentState
    """

    prompt_template = ChatPromptTemplate.from_template(template)

    model = ChatGroq(
        model = "openai/gpt-oss-120b",
        # model = "openai/gpt-oss-safeguard-20b",
        api_key=GROQ_API_KEY
    )

    model = model.bind_tools([
        get_current_date_time,
        search_the_web
    ])

    chain = prompt_template | model


    answer = chain.invoke(state["messages"])

    return {"messages" : [answer]}