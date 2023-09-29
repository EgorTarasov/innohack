from pydantic import BaseModel, Field, ConfigDict
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Table, Enum
from sqlalchemy.orm import relationship, Mapped, mapped_column, DeclarativeBase
from app.db import BaseSqlModel
import enum


# enums
class Level(enum.Enum):
    low = "low"
    medium = "medium"
    high = "high"


# models

class Ticket(BaseSqlModel):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)

    duration = Column(Integer)
    competences = relationship(
        "Competence",
        back_populates="tickets",
        secondary="ticket_competition",
    )
    level = Column(Enum(Level))
    author_id = Column(Integer, ForeignKey("users.id"))
    worker_id = Column(Integer, ForeignKey("users.id"))
    due_date = Column(DateTime)

    author = relationship(
        "User",
        back_populates="created_tickets",
        primaryjoin="User.id==Ticket.author_id",
    )
    worker = relationship(
        "User",
        back_populates="taken_tickets",
        primaryjoin="User.id==Ticket.worker_id",
    )


class TicketCreate(BaseModel):
    email: str
    username: str
    password: str


# связи

ticket_competition = Table(
    "ticket_competence",
    BaseSqlModel.metadata,
    Column("ticket_id", ForeignKey("Ticket.id")),
    Column("competence_id", ForeignKey("Competence.id")),
)
