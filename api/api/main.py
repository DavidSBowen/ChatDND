from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    HumanMessage,
    SystemMessage,
    AIMessage,
    BaseMessage
)
import uvicorn
import uuid
import asyncio

from models import (
    ChatMessage,
    PlayerMessage,
    DMMessage,
    Player
)

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
    response = await send_chat_message(message.content)
    return response

class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: ChatMessage, websocket: WebSocket):
        await websocket.send_text(message.json())

    async def broadcast_others(self, message: ChatMessage, websocket: WebSocket):
        for connection in self.active_connections:
            if connection != websocket:
                await connection.send_text(message.json())

    async def broadcast(self, message: ChatMessage):
        for connection in self.active_connections:
            await connection.send_text(message.json())


manager = ConnectionManager()

@app.websocket("/chat/ws")
async def chat_websocket(websocket: WebSocket):
    id = str(uuid.uuid4())
    player = Player(id=id)
    await manager.connect(websocket)
    try:
        while True:
            req: dict = await websocket.receive_json()
            req['player'] = player
            message = PlayerMessage.parse_obj(req)
            await manager.broadcast_others(message, websocket)

            response = await send_chat_message(message.content)
            dmMessage = DMMessage(content=response)
            await manager.broadcast(dmMessage)

    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"left the chat")

async def send_chat_message(message: str) -> str:
    humanMessage = HumanMessage(content=message)
    loop = asyncio.get_event_loop()
    messages.append(humanMessage)
    res: AIMessage = await loop.run_in_executor(None, lambda: chat(messages))
    messages.append(res)
    return res.content

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)