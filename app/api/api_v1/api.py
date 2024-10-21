# app/api/api_v1/api.py
from fastapi import APIRouter
from app.api.api_v1.endpoints import auth, user, chat

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(user.router, prefix="/users", tags=["users"])
api_router.include_router(chat.router, prefix="/chat", tags=["chat"])