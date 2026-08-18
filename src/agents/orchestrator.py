from src.models.schemas import KascadeState
from src.utils.tracing import trace_agent


def orchestrator(state: KascadeState) -> dict:
    """
    Procedural orchestrator.

    It does not perform semantic reasoning.
    It only coordinates lifecycle transitions.
    """

    trace_agent(
        agent_name="ORCHESTRATOR",
        message="Evaluating current lifecycle state.",
        data={
            "has_intent": state.intent is not None,
            "candidate_count": len(state.candidate_services),
            "has_selection": state.selection is not None,
        },
    )

    return {
        "current_agent": "Orchestrator",
        "status": "ROUTING",
    }


def route_next_agent(state: KascadeState) -> str:
    """
    Determine the next lifecycle stage.
    """

    # Stage 1: Intent interpretation
    if state.intent is None:
        return "intent_interpreter"

    # Stage 2: Service discovery
    if not state.candidate_services:
        return "service_discovery"

    # Stage 3: Service selection
    if state.selection is None:
        return "service_selector"

    # Workflow completed
    return "orchestrator_finalize"


def orchestrator_finalize(state: KascadeState) -> dict:

    intent = state.intent
    selection = state.selection

    response = f"""
KASCADE Composition Result

User Request:
{state.user_request}

Interpreted Intent:
{intent.goal}

Required Capabilities:
{", ".join(intent.required_capabilities)}

Selected Services:
{", ".join(selection.selected_services)}

Reason:
{selection.justification}
"""

    trace_agent(
        agent_name="ORCHESTRATOR",
        message="KASCADE composition workflow completed.",
        data={
            "selected_services": selection.selected_services
        },
    )

    return {
        "current_agent": "Orchestrator",
        "status": "COMPLETED",
        "final_response": response,
    }