from app.crud.base import CRUDBase
from app.models.chat import Chat
from app.schemas.chat import ChatCreate, ChatUpdate

CRUDChat = CRUDBase[Chat, ChatCreate, ChatUpdate]
crud_chat = CRUDChat(Chat)