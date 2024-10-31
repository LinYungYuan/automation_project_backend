from pydantic import BaseModel
from typing import List, Optional
from app.models.chats import (
    Chat
)
class ProcessRequest(BaseModel):
    chatId: str
    userId: str
    history: List[Chat]
    userContent: str

class ChatBase(BaseModel):
    chatId: str
    userId: str
    userContent: str
    assistantContent: str
    
# Pydantic schemas
class ChatCreate(BaseModel):
    chatId: str
    userId: str
    userContent: Optional[str] = None
    assistantContent: Optional[str] = None
    
# Pydantic schemas
class ChatUpdate(BaseModel):
    chatId: str
    userId: str
    userContent: Optional[str] = None
    assistantContent: Optional[str] = None
    
class ChatDelete(BaseModel):
    chatId : str