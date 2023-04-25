from fastapi import FastAPI, WebSocket
from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate, LLMChain
from langchain.prompts.chat import (
    ChatMessagePromptTemplate,
    SystemMessagePromptTemplate, 
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate
)
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage,
    BaseMessage
)

app = FastAPI()
chat = ChatOpenAI(temperature=0)
messages: list[BaseMessage] = [
    # SystemMessage("You are a helpful AI assistant.")
]

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/chat/")
async def receive_message(message: HumanMessage):
    response = send_chat_message(message)
    return response

@app.websocket("/chat/ws")
async def chat_websocket(websocket: WebSocket):
    await websocket.accept()
    while True:
        message = await websocket.receive_text()
        response = send_chat_message(HumanMessage(message))
        websocket.send_text(response.content)

def send_chat_message(message: HumanMessage):
    messages.append(message)
    res = chat(messages)
    messages.append(res)
    return res