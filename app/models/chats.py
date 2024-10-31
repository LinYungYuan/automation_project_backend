from sqlalchemy import Column, ForeignKey, Integer, String, Time
import datetime
from app.models.base import Base


class Chat(Base):
    chatId = Column(Integer, primary_key=True, index=True)
    userId = Column(Integer, ForeignKey("user.id"), index=True)
    assistantContent = Column(String)
    userContent = Column(String)
    userContentTime = Column(Time(), default=datetime.datetime.now().time)
    assistantContentTime = Column(Time(), default=datetime.datetime.now().time)
