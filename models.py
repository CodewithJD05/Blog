
from sqlalchemy import Column, String,Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from database import Base

# Blog Table

class Blog(Base):
    __tablename__ = "blogs"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)

  