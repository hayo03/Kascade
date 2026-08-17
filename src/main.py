from dotenv import load_dotenv

load_dotenv()
import os

print("API key loaded:", bool(os.getenv("OPENAI_API_KEY")))
from src.models.schemas import KascadeState
from src.graph.workflow import build_graph


def main():

    graph = build_graph()

    user_request = """
    I need a low-latency video streaming service
    for autonomous vehicles with latency below 20ms.
    """

    initial_state = KascadeState(
        user_request=user_request
    )

    result = graph.invoke(initial_state)

    print("\n==============================")
    print("KASCADE DEMO")
    print("==============================")

    print("\nFinal status:")
    print(result["status"])

    print("\nInterpreted intent:")
    print(result["intent"])

    print("\nSelected services:")
    print(result["selection"])

    print("\nFinal response:")
    print(result["final_response"])


if __name__ == "__main__":
    main()