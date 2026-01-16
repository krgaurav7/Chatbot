from langgraph.graph import START, END, StateGraph
from langgraph.graph.state import CompiledStateGraph
from src.agents.chat_agent.states.chat_agent_state import ChatAgentState
from agents.chat_agent.nodes.tool_executor_node import tool_executor_node
from src.agents.chat_agent.nodes.should_continue import should_continue
from src.agents.chat_agent.nodes.chat_node import chat
from langgraph.checkpoint.memory import MemorySaver

checkpointer = MemorySaver()

def create_chat_agent_graph_builder() -> CompiledStateGraph:
    """
    Docstring for create_chat_agent_graph_builder
    """
    graph_builder = StateGraph(ChatAgentState)

    graph_builder.add_node("chat_node", chat)
    graph_builder.add_node("tool_executor_node", tool_executor_node)

    graph_builder.add_edge(START, "chat_node")
    graph_builder.add_conditional_edge(
        "chat_node",
        should_continue
    )

    graph_builder.add_edge("tool_executor_node", "chat_node")

    return graph_builder.compile(checkpointer = checkpointer)