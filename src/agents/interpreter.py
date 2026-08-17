from dotenv import load_dotenv

load_dotenv()

from langchain_openai import ChatOpenAI

from src.models.schemas import (
    KascadeState,
    Intent
)
from src.utils.tracing import trace_agent


llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)


interpreter_llm = llm.with_structured_output(
    Intent,
    method="function_calling"
)


def interpret_intent(state: KascadeState) -> dict:

    prompt = f"""
You are the Intent Interpretation Agent of KASCADE.

Your task is to transform a natural-language service request
into a structured service intent.

User request:

{state.user_request}

Extract:

1. The main goal.
2. The application domain if available.
3. Required service capabilities.
4. Explicit or implicit technical constraints.

Examples of capabilities:

- video_streaming
- low_latency
- edge_compute
- object_detection
- storage
- connectivity

Return ONLY the structured intent.
"""

    intent = interpreter_llm.invoke(prompt)
    trace_agent(
    agent_name="INTENT INTERPRETER",
    message="Natural-language request interpreted.",
    data=intent.model_dump()
)

    return {
        "intent": intent,
        "current_agent": "IntentInterpreter",
        "status": "INTENT_INTERPRETED"
    }