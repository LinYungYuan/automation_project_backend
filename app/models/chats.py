from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from app.models.base import Base
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

class Chat(Base):
    chat_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.user_id"), index=True)
    title = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    messages = relationship("Message", back_populates="chat")
    user = relationship("User")
    