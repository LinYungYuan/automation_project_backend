from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel, ConfigDict

# 聊天室相關Schema
class ChatBase(BaseModel):
    title: str

class ChatRoomCreate(ChatBase):
    pass

class ChatRoomUpdate(ChatBase):
    title: Optional[str] = None

class ChatRoomOut(ChatBase):
    id: int
    user_id: int
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)