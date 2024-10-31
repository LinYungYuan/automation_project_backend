from app.crud.base import CRUDBase
from app.models.chats import Chat
from app.schemas.chat import ChatBase

CRUDChat = CRUDBase[Chat, ChatBase]
crud_chat = CRUDChat(Chat)