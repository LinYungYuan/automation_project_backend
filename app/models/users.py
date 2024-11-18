from sqlalchemy import Boolean, Column, Integer, String
from app.models.base import Base

#db的欄位定義
class User(Base):
    user_id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
