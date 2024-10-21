# app/api/api_v1/endpoints/chat.py
from fastapi import APIRouter, Depends
from typing import List
from app.api.deps import get_current_user
from app.models.user import User
from app.schemas.chat import Message, MessageCreate
from app.services.chat import get_chat_messages, create_chat_message

router = APIRouter()

@router.get("/", response_model=List[Message])
async def read_messages(current_user: User = Depends(get_current_user)):
    return get_chat_messages(current_user)

@router.post("/", response_model=Message)
async def create_message(message: MessageCreate, current_user: User = Depends(get_current_user)):
    return create_chat_message(current_user, message)