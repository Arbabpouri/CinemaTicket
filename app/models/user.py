from sqlalchemy import String, Integer
from sqlalchemy.orm import mapped_column, Mapped
from settings.database import Base


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    usernaem: Mapped[str] = mapped_column(String(250), unique=True)
    email: Mapped[str] = mapped_column(String(250), unique=True)
    password: Mapped[str]
    