from langgraph.graph import StateGraph, START, END

from src.models.schemas import KascadeState

from src.agents.orchestrator import (
    orchestrator_start,
    orchestrator_finalize
)

from src.agents.interpreter import (
    interpret_intent
)

from src.agents.discovery import (
    discover_services
)

from src.agents.selector import (
    select_services
)


def build_graph():

    graph = StateGraph(KascadeState)

    # --------------------------------
    # Nodes
    # --------------------------------

    graph.add_node(
        "orchestrator_start",
        orchestrator_start
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

    # --------------------------------
    # Workflow
    # --------------------------------

    graph.add_edge(
        START,
        "orchestrator_start"
    )

    graph.add_edge(
        "orchestrator_start",
        "intent_interpreter"
    )

    graph.add_edge(
        "intent_interpreter",
        "service_discovery"
    )

    graph.add_edge(
        "service_discovery",
        "service_selector"
    )

    graph.add_edge(
        "service_selector",
        "orchestrator_finalize"
    )

    graph.add_edge(
        "orchestrator_finalize",
        END
    )

    return graph.compile()