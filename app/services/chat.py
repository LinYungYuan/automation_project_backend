# app/services/chat.py
from typing import List
from sqlalchemy.orm import Session
from app.models.user import User
from app.models.chat import Message
from app.schemas.chat import MessageCreate

def get_chat_messages(db: Session, user: User) -> List[Message]:
    return db.query(Message).filter(Message.sender == user.username).all()

def create_chat_message(db: Session, user: User, message: MessageCreate) -> Message:
    return Message.create(db, sender=user.username, content=message.content)