from datetime import datetime
from typing import List
from pydantic import BaseModel, ConfigDict
from app.schemas.chat import ChatRoomOut

# BaseModel使用來資料驗證跟結構定義
# 訊息相關Schema
class MessageBase(BaseModel):
    chat_id: int
    message_id: int
    content: str
    is_bot: bool = False

class MessageCreate(BaseModel):
    chat_id: int
    content: str
    is_bot: bool = False
    created_at: datetime
    update_at: datetime

class MessageOut(MessageBase):
    created_at: datetime
    update_at: datetime
    
    
# 訊息相關Schema
class MessageRequest(BaseModel):
    chat_id: str
    is_bot: bool = False
    content: str