from src.models.schemas import KascadeState
from src.knowledge.service_catalog import get_service_catalog
from src.utils.tracing import trace_agent


def discover_services(state: KascadeState) -> dict:

    intent = state.intent

    catalog = get_service_catalog()

    required_capabilities = set(
        intent.required_capabilities
    )

    discovered_services = []

    for service in catalog:

        service_capabilities = set(
            service.capabilities
        )

        matching_capabilities = (
            required_capabilities
            & service_capabilities
        )

        if matching_capabilities:
            discovered_services.append(service)

    trace_agent(
        agent_name="SERVICE DISCOVERY",
        message="Candidate services discovered.",
        data={
            "requested_capabilities":
                intent.required_capabilities,

            "number_of_candidates":
                len(discovered_services),

            "candidate_services": [
                {
                    "service_id": service.service_id,
                    "name": service.name,
                    "capabilities": service.capabilities
                }
                for service in discovered_services
            ]
        }
    )

    return {
        "candidate_services": discovered_services,
        "current_agent": "ServiceDiscovery",
        "status": "SERVICES_DISCOVERED"
    }