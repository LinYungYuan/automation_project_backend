# app/models/chat.py
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import Session
from app.core.db_session import Base
from datetime import datetime

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    sender = Column(String, ForeignKey("users.username"))
    content = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)

    @classmethod
    def create(cls, db: Session, sender: str, content: str):
        db_msg = cls(sender=sender, content=content)
        db.add(db_msg)
        db.commit()
        db.refresh(db_msg)
        return db_msg