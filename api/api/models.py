from pydantic import BaseModel

class Player(BaseModel):
    id: str

class ChatMessage(BaseModel):
    content: str

class PlayerMessage(ChatMessage):
    player: Player

class DMMessage(ChatMessage):
    pass
