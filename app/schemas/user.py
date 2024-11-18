from typing import Optional
from pydantic import BaseModel, EmailStr, ConfigDict


class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    is_active: bool = True
    is_superuser: bool = False
    full_name: Optional[str] = None

class UserCreate(UserBase):
    email: EmailStr
    password: str

class UserOut(UserBase):
    user_id: int
    model_config = ConfigDict(from_attributes=True)

class UserInDB(UserBase):
    hashed_password: str

class UserUpdate(UserBase):
    password: Optional[str] = None

class UserUpdateDB(UserBase):
    hashed_password: str
