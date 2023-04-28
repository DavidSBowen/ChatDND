from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    HumanMessage,
    SystemMessage,
    BaseMessage
)
import uvicorn

app = FastAPI()
origins = [
    "*",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

chat = ChatOpenAI(temperature=0)
messages: list[BaseMessage] = [
    SystemMessage(content="You are a helpful AI assistant.")
]

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/chat/")
async def receive_message(message: HumanMessage):
    response = send_chat_message(message)
    return response

class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()

@app.websocket("/chat/ws")
async def chat_websocket(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            message = await websocket.receive_text()
            response = send_chat_message(HumanMessage(content=message))
            await websocket.send_text(response.content)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"left the chat")

def send_chat_message(message: HumanMessage):
    messages.append(message)
    res = chat(messages)
    messages.append(res)
    return res

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)