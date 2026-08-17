from typing import Any


def trace_agent(
    agent_name: str,
    message: str,
    data: Any = None
):
    print("\n" + "=" * 70)
    print(f"[KASCADE TRACE] {agent_name}")
    print("=" * 70)

    print(message)

    if data is not None:
        print("\nDATA:")
        print(data)

    print("=" * 70)