from fastapi import APIRouter, HTTPException
import httpx
from fastapi import Depends
from app.crud.chat import crud_chat
from app.crud.message import crud_message
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.chats import Chat
from app.models.message import Message
from app.models.users import User
from app.schemas.chat import (
    ChatRoomCreate,
    ChatBase
)
from app.api.deps import (
    get_current_user,
    get_session
)
from app.schemas.message import MessageBase, MessageRequest

router = APIRouter(prefix="/rooms", tags=["Tasks"])
#建立聊天室
@router.post("/", response_model=ChatRoomCreate, summary="新增聊天室")
async def create_chat_room(
    chat: ChatRoomCreate,
    db: AsyncSession = Depends(get_session),
    current_user = Depends(get_current_user)
):
    chat_room = Chat(
        user_id=current_user.id,
        title=chat.title
    )
    # Create the chat room in the database
    await crud_chat.create(db, chat_room)
    return chat_room

# 取得聊天室內容
@router.get("/chat/{chat_id}", status_code=201,summary="取得聊天室歷史內容")
async def process_chat(
    chat_id: str,
    current_user = Depends(get_current_user), 
    db: AsyncSession = Depends(get_session)
) -> MessageBase:
    try:
        messgae = Message(
            user_id=current_user.id,
            chat_id=chat_id
        )
        await crud_message.get(db, messgae)
        return messgae
    except httpx.RequestError as e:
        raise HTTPException(
            status_code=503,
            detail=f"無法連接到處理服務: {str(e)}"
        )


# 發送訊息
@router.post("/chat/{chat_id}message", status_code=201,description="與ai串接")
async def process_chat(
    chat_id: str,
    messageRequest: MessageRequest,
    db: AsyncSession = Depends(get_session)
) -> ChatBase:
    try:
        ##將Pydantic模型轉換為字典，方便存入資料庫
        req_body = messageRequest.model_dump().pop("chat_id", chat_id)
        # 等待 API 回應時，可以處理其他任務
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "http://localhost:8011/process",
                json=req_body 
            )
            
            if response.status_code != 200:
                raise HTTPException(
                    status_code=response.status_code,
                    detail="處理請求時發生錯誤"
                )
            res = MessageBase.model_validate_json(response.json())
            chat = await crud_chat.create(db, res)
            
            return chat
        
    except httpx.RequestError as e:
        raise HTTPException(
            status_code=503,
            detail=f"無法連接到處理服務: {str(e)}"
        )