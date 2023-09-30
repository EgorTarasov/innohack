# define level class from sqlbase class and define levelsDto

from pydantic import BaseModel, Field, ConfigDict
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean, DateTime, ForeignKey
from app.db import BaseSqlModel


class Level(BaseSqlModel):
    __tablename__ = "levels"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    label: Mapped[str] = mapped_column(String, index=True)

    def __repr__(self):
        return f"<Level {self.label}>"


class LevelDto(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": 1,
                "label": "Junior",
            }
        },
    )

    id: int = Field(...)
    label: str = Field(...)


class LevelCreate(BaseModel):
    label: str = Field(...)
