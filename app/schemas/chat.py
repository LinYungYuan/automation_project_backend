from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel, ConfigDict

# 聊天室相關Schema
class ChatBase(BaseModel):
    title: str

class ChatCreate(ChatBase):
    pass

class ChatUpdate(ChatBase):
    title: Optional[str] = None

class ChatOut(ChatBase):
    id: int
    user_id: int
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)