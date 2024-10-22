from sqlalchemy.orm import Session
from app.models.chat import Message
from app.models.user import User
from app.schemas.chat import MessageCreate

def get_messages(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Message).order_by(Message.timestamp.desc()).offset(skip).limit(limit).all()

def create_message(db: Session, message: MessageCreate, user: User):
    db_message = Message(content=message.content, sender_id=user.id)
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message

def get_user_messages(db: Session, user: User, skip: int = 0, limit: int = 100):
    return db.query(Message).filter(Message.sender_id == user.id).order_by(Message.timestamp.desc()).offset(skip).limit(limit).all()