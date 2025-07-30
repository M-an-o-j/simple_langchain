from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from agent import run_mcp_agent

app = FastAPI()

@app.websocket("/ws/ask")
async def websocket_endpoint(websocket: WebSocket):
    """
    WebSocket /ws/ask

    Allows real-time communication with the MCP agent.
    Accepts natural language messages via WebSocket and returns the AI-generated response.

    Usage:
        Client connects and sends a message string (the query).
        Server responds with the result from the LangChain agent.

    On disconnect, the connection is closed gracefully.
    """
    await websocket.accept()
    try:
        while True:
            query = await websocket.receive_text()
            try:
                response = run_mcp_agent(query)
                print(response)
                await websocket.send_text(response["output"])
            except Exception as e:
                await websocket.send_text(f"Error: {str(e)}")
    except WebSocketDisconnect:
        print("WebSocket connection closed")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
