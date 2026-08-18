from langgraph.graph import StateGraph, START, END

from src.models.schemas import KascadeState

from src.agents.orchestrator import (
    orchestrator,
    route_next_agent,
    orchestrator_finalize,
)

from src.agents.interpreter import interpret_intent
from src.agents.discovery import discover_services
from src.agents.selector import select_services


def build_graph():

    graph = StateGraph(KascadeState)

    # -----------------------------------
    # Nodes
    # -----------------------------------

    graph.add_node(
        "orchestrator",
        orchestrator
    )

    graph.add_node(
        "intent_interpreter",
        interpret_intent
    )

    graph.add_node(
        "service_discovery",
        discover_services
    )

    graph.add_node(
        "service_selector",
        select_services
    )

    graph.add_node(
        "orchestrator_finalize",
        orchestrator_finalize
    )

    # -----------------------------------
    # Start
    # -----------------------------------

    graph.add_edge(
        START,
        "orchestrator"
    )

    # -----------------------------------
    # Dynamic routing
    # -----------------------------------

    graph.add_conditional_edges(
        "orchestrator",
        route_next_agent,
        {
            "intent_interpreter": "intent_interpreter",
            "service_discovery": "service_discovery",
            "service_selector": "service_selector",
            "orchestrator_finalize": "orchestrator_finalize",
        },
    )

    # -----------------------------------
    # Return control to orchestrator
    # -----------------------------------

    graph.add_edge(
        "intent_interpreter",
        "orchestrator"
    )

    graph.add_edge(
        "service_discovery",
        "orchestrator"
    )

    graph.add_edge(
        "service_selector",
        "orchestrator"
    )

    # -----------------------------------
    # End
    # -----------------------------------

    graph.add_edge(
        "orchestrator_finalize",
        END
    )

    return graph.compile()