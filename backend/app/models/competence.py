from pydantic import BaseModel, Field, ConfigDict
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.db import BaseSqlModel


class Competence(BaseSqlModel):
    __tablename__ = "competences"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    tickets = relationship("Ticket", back_populates="competences", secondary="ticket_competence")
