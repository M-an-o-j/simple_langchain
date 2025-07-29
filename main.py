from fastapi import FastAPI, Request
from pydantic import BaseModel
from agent import run_mcp_agent

app = FastAPI()

class Query(BaseModel):
    query: str

@app.post("/ask")
async def ask_agent(payload: Query):
    """
    POST /ask

    Runs the MCP AI agent on the input query and returns the response.

    Args:
        payload (Query): A JSON object with a single key, "query", which is the
            input for the AI agent.

    Returns:
        dict: A JSON object with either a "response" or an "error" key.
            "response" contains the output of the AI agent.
            "error" contains a string describing the error if the AI agent
                fails.
    """
    try:
        response = run_mcp_agent(payload.query)
        return {"response": response}
    except Exception as e:
        return {"error": str(e)}
    

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
