
from fastapi import APIRouter, Depends
from sqlalchemy import select
from typing import Optional
from app.api.deps import get_token_data
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.config import settings
from app.core.database import SessionLocal
from app.core.logger import get_logger
from app.core.security import get_password_hash
from app.models.users import User

logger = get_logger(__name__)
router = APIRouter(prefix="/home", tags=["Home"])

@router.get("/", dependencies=[Depends(get_token_data)])
async def home():
    return "Hello World!"

@router.get("/another/")
async def another():
    logger.info("Creating initial data")
    async with SessionLocal() as session:
        await create_first_user(session)
    logger.info("Initial data created")

    return "Another Hello World!"


async def create_first_user(session: AsyncSession) -> None:
    email = settings.FIRST_USER_EMAIL
    password = get_password_hash(settings.FIRST_USER_PASSWORD.get_secret_value())
    result = await session.execute(select(User).where(User.email == email))
    user: Optional[User] = result.scalars().first()
    if user is None:
        session.add(User(email=email, hashed_password=password, is_superuser=True))
        await session.commit()