from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.sql.functions import now

from chatapp.database import Base


class Message(Base):
    __tablename__ = "message"
    id: Mapped[int] = mapped_column(primary_key=True)
    receiver_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    sender_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    content: Mapped[str]
    timestamp: Mapped[datetime] = mapped_column(server_default=now())

    def __init__(self, receiver_id, sender_id, content):
        self.receiver_id = receiver_id
        self.sender_id = sender_id
        self.content = content
