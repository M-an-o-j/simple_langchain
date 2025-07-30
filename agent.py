from langchain.agents import initialize_agent, Tool
from langchain_openai import ChatOpenAI
from tools import calculator, greet, paper_game, light_on, light_off
import os

llm = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    openai_api_key="openrouter_api_key",
    openai_api_base="https://openrouter.ai/api/v1",  # Optional for OpenRouter
)

tools = [
    Tool(
        name="Paper Game",
        func=paper_game,
        description="Play rock-paper-scissors. Use only 'rock', 'paper', or 'scissors'."
    ),
    Tool(
        name="Calculator",
        func=calculator,
        description="Use this tool **only** when a user asks to do math, like 'what is 2+2' or 'calculate 5 * (3 + 1)'."
    ),
    Tool(
        name="Greeter",
        func=greet,
        description="Use this to respond when someone says 'hi', 'hello', or greets you."
    ),
    Tool(
        name="Lights on",
        func=light_on,
        description="Turn the lights on. when user want light"
    ),
    Tool(
        name="Lights off",
        func=light_off,
        description="Turn the lights off. when user want light"
    )
]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent="zero-shot-react-description",
    handle_parsing_errors=True,
    max_iterations=10
)

def run_mcp_agent(query: str) -> str:
    """
    Run the agent on the given query.

    The agent is an AI that processes natural language and determines what
    tool to use to respond to the query. The tools are defined in the
    `tools` list above.

    Parameters
    ----------
    query : str
        The natural language query to process.

    Returns
    -------
    str
        The response from the agent.
    """
    return agent.invoke(query)
