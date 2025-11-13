from langgraph.graph import StateGraph, END
from .state import AgentState
from .nodes import (
    data_retrieval_node,
    data_analysis_node,
    web_search_node,
    viz_node,
    report_generator_node,
)

def _should_web_search(state: AgentState) -> str:
    use_web = bool(state.get("params", {}).get("use_web", False))
    return "web" if use_web else "skip_web"

def build_graph():
    g = StateGraph(AgentState)

    g.add_node("data_retrieval", data_retrieval_node)
    g.add_node("data_analysis", data_analysis_node)
    g.add_node("web_search", web_search_node)
    g.add_node("viz", viz_node)
    g.add_node("report", report_generator_node)

    g.set_entry_point("data_retrieval")
    g.add_edge("data_retrieval", "data_analysis")

    # conditional branch for web
    g.add_conditional_edges(
        "data_analysis",
        _should_web_search,
        {
            "web": "web_search",
            "skip_web": "viz",
        },
    )
    g.add_edge("web_search", "viz")
    g.add_edge("viz", "report")
    g.add_edge("report", END)

    return g.compile()
