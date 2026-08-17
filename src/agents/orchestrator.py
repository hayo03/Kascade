from src.models.schemas import KascadeState
from src.utils.tracing import trace_agent


def orchestrator_start(state: KascadeState) -> dict:

    trace_agent(
        agent_name="ORCHESTRATOR",
        message="Starting KASCADE workflow.",
        data={
            "user_request": state.user_request
        }
    )

    return {
        "current_agent": "Orchestrator",
        "status": "STARTED"
    }


def orchestrator_finalize(state: KascadeState) -> dict:

    intent = state.intent
    selection = state.selection

    selected_ids = selection.selected_services

    response = f"""
KASCADE Composition Result

User Request:
{state.user_request}

Interpreted Intent:
{intent.goal}

Required Capabilities:
{", ".join(intent.required_capabilities)}

Selected Services:
{", ".join(selected_ids)}

Reason:
{selection.justification}
"""

    trace_agent(
        agent_name="ORCHESTRATOR",
        message="Composition workflow completed.",
        data={
            "selected_services": selected_ids,
            "status": "COMPLETED"
        }
    )

    return {
        "current_agent": "Orchestrator",
        "status": "COMPLETED",
        "final_response": response
    }