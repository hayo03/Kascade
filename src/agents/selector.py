from dotenv import load_dotenv

load_dotenv()


from langchain_openai import ChatOpenAI

from src.models.schemas import (
    KascadeState,
    ServiceSelection
)


llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)


selector_llm = llm.with_structured_output(
    ServiceSelection,
    method="function_calling"
)


def select_services(state: KascadeState) -> dict:

    intent = state.intent

    services_description = "\n".join(
        [
            f"""
Service ID: {service.service_id}
Name: {service.name}
Capabilities: {service.capabilities}
Domain: {service.domain}
Properties: {service.properties}
"""
            for service in state.candidate_services
        ]
    )

    prompt = f"""
You are the Service Selection Agent of KASCADE.

You must select the services that best satisfy the interpreted intent.

INTERPRETED INTENT:

Goal:
{intent.goal}

Domain:
{intent.domain}

Required capabilities:
{intent.required_capabilities}

Constraints:
{intent.constraints}


AVAILABLE SERVICES:

{services_description}


Selection rules:

1. Prefer services matching the required capabilities.
2. Prefer services matching the requested domain.
3. Respect technical constraints.
4. Do not select a service if it clearly cannot satisfy the intent.
5. Explain the selection briefly.

Return ONLY the structured service selection.
"""

    selection = selector_llm.invoke(prompt)

    return {
        "selection": selection,
        "current_agent": "ServiceSelector",
        "status": "SERVICES_SELECTED"
    }