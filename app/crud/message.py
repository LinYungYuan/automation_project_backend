from app.crud.base import CRUDBase
from app.models.message import Message
from app.schemas.message import MessageCreate, MessageOut

CRUDMessage = CRUDBase[Message, MessageCreate, MessageOut]
crud_message = CRUDMessage(Message)