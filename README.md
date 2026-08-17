# KASCADE Demo

A minimal **LangGraph-based multi-agent prototype** for intent-driven service composition.

The current demo implements:

**Orchestrator → Intent Interpreter → Service Discovery → Service Selector → Orchestrator**

## Quick Start

### 1. Create a virtual environment

```bash
python -m venv .venv
Activate it on Windows:

.venv\Scripts\activate
2. Install dependencies
pip install -r requirements.txt
3. Configure the OpenAI API key

Create a .env file in the project root:

OPENAI_API_KEY=your_api_key_here

Do not commit the .env file to GitHub.

4. Run the demo

From the project root:

python -m src.main

The demo interprets the user request, discovers candidate services, selects the most suitable service, and returns the final composition result