from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean
from app.models.base import Base
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship


class Message(Base):
    
    message_id = Column(Integer, primary_key=True, index=True)
    chat_id = Column(Integer, ForeignKey("chat.chat_id"))
    content = Column(String)
    is_bot = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    chat = relationship("Chat", back_populates="messages")