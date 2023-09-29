from pydantic import BaseModel, Field, ConfigDict
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.db import BaseSqlModel


class User(BaseSqlModel):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)

    created_tickets = relationship(
        "Ticket", back_populates="author", primaryjoin="User.id==Ticket.author_id"
    )
    taken_tickets = relationship(
        "Ticket", back_populates="worker", primaryjoin="User.id==Ticket.worker_id"
    )


class UserCreate(BaseModel):
    email: str
    username: str
    password: str


class UserLogin(BaseModel):
    email: str
    password: str
