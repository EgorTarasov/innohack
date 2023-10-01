from app import schemas
from app.db import BaseSqlModel
from pydantic import BaseModel, ConfigDict, Field
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Sprint(BaseSqlModel):
    __tablename__ = "sprints"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    duration: Mapped[int] = mapped_column(Integer)  # длительность спринта в неделях
    target: Mapped[str] = mapped_column(String)
    is_finished: Mapped[bool] = mapped_column(Boolean, default=False)
    value: Mapped[dict] = mapped_column(JSONB, default={})


class SprintDto(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": 1,
                "duration": 1,
                "target": "test",
                "is_finished": False,
                "users": [
                    {
                        "user_data": {"id": 2, "username": "Иван Иванов", "hours": 20},
                        "tickets": [
                            {
                                "id": 42,
                                "sprint_id": None,
                                "title": "Ticket 2 Title",
                                "description": "Ticket 2 Description",
                                "reporter_id": 2,
                                "assignee_id": 3,
                                "due_date": "2022-01-02T00:00:00",
                                "roles": {"id": 13, "label": "Frontend"},
                                "level": {"id": 9, "label": "Senior"},
                            }
                        ],
                    }
                ],
            }
        },
    )
    # FIXME распределенная задача - задача с sprint_id
    id: int = Field(..., alias="id")
    target: str = Field(...)
    duration: int = Field(..., ge=1, le=5)
    is_finished: bool = Field(..., alias="is_finished")

    users: list[dict] = Field(...)


class UserLoad(BaseModel):
    id: int = Field(...)
    hours: int = Field(...)


class SprintCreate(BaseModel):
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "target": "Выйграть InnoHack",
                "duration": 1,
                "users": [
                    {
                        "id": 1,
                        "hours": 38,
                    },
                    {"id": 2, "hours": 38},
                ],
            }
        }
    )

    target: str = Field(...)
    duration: int = Field(..., ge=1, le=5, description="Длительность спринта в неделях")
    users: list[UserLoad] = Field(...)
