# app/api/api_v1/endpoints/user.py
from fastapi import APIRouter, Depends
from app.api.deps import get_current_user
from app.models.user import User
from app.schemas.user import UserUpdate

router = APIRouter()

@router.get("/me")
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

@router.put("/me")
async def update_user_me(user_update: UserUpdate, current_user: User = Depends(get_current_user)):
    updated_user = current_user.update(user_update)
    return updated_user