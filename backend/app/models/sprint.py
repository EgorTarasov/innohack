from pydantic import BaseModel, Field, ConfigDict
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.db import BaseSqlModel


class Sprint(BaseSqlModel):
    __tablename__ = "sprints"

    id = Column(Integer, primary_key=True, index=True)
    duration = Column(Integer)  # длительность спринта в днях
    target = Column(String)
    is_finished = Column(Boolean)
