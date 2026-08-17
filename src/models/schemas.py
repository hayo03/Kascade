from typing import Dict, List, Optional
from pydantic import BaseModel, Field


class Intent(BaseModel):
    """
    Structured representation of the interpreted user intent.
    """

    goal: str = Field(
        description="The main goal expressed by the user."
    )

    domain: str = Field(
        description="The application or service domain."
    )

    required_capabilities: List[str] = Field(
        description="Capabilities required to satisfy the intent."
    )

    constraints: Dict[str, str] = Field(
        description="Technical or business constraints."
    )


class Service(BaseModel):
    """
    Representation of a concrete service offer.
    """

    service_id: str

    name: str

    capabilities: List[str]

    domain: str

    properties: Dict[str, str]


class ServiceSelection(BaseModel):
    """
    Result produced by the Service Selector Agent.
    """

    selected_services: List[str] = Field(
        description="IDs of the selected services."
    )

    justification: str = Field(
        description="Explanation for why the services were selected."
    )
class KascadeState(BaseModel):
    """
    Shared state exchanged between the LangGraph nodes.
    """

    user_request: str

    intent: Optional[Intent] = None

    candidate_services: List[Service] = Field(
        default_factory=list
    )

    selection: Optional[ServiceSelection] = None

    current_agent: Optional[str] = None

    status: str = "STARTED"

    final_response: Optional[str] = None