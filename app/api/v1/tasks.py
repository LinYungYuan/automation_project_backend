from fastapi import APIRouter, HTTPException
import httpx
from fastapi import Depends
from app.crud.chat import crud_chat
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.chat import (
    ProcessRequest,
    ChatBase
)
from app.api.deps import (
    get_session
)

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("/", status_code=201)
async def process_chat(
    request: ProcessRequest,
    db: AsyncSession = Depends(get_session)
) -> ChatBase:
    try:
        # 等待 API 回應時，可以處理其他任務
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "http://localhost:8011/process",
                json=request.model_dump()
            )
            
            if response.status_code != 200:
                raise HTTPException(
                    status_code=response.status_code,
                    detail="處理請求時發生錯誤"
                )
            res = ChatBase.model_validate_json(response.json())
            chat = await crud_chat.create(db, res)
            
            return chat
        
    except httpx.RequestError as e:
        raise HTTPException(
            status_code=503,
            detail=f"無法連接到處理服務: {str(e)}"
        )
    