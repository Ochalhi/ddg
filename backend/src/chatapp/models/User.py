from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from chatapp.database import Base


class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
