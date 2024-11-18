from app.crud.base import CRUDBase
from app.models.message import Message
from app.schemas.message import MessageBase

CRUDMessage = CRUDBase[Message, MessageBase]
crud_message = CRUDMessage(Message)