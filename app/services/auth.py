# app/services/auth.py
from sqlalchemy.orm import Session
from app.core.security import verify_password
from app.models.user import User

def authenticate_user(db: Session, username: str, password: str):
    user = User.get(db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user