from datetime import datetime

from app import models
from pydantic import BaseModel, ConfigDict, Field


class TicketDto(BaseModel):
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "id": 1,
                "sprint_id": 1,
                "title": "test",
                "description": "test",
                "reporter_id": 1,
                "assignee_id": 2,
                "due_date": "2021-01-01",
                "durations": [1, 2, 4],
                "role": {"role_id": 1, "label": "Frontend"},
                "level": {"level_id": 1, "label": "Junior"},
                "priority": 2,
            }
        },
    )

    id: int = Field(..., alias="id")
    sprint_id: int | None = Field(None, alias="sprint_id")
    title: str = Field(..., alias="title")
    description: str = Field(..., alias="description")
    reporter_id: int = Field(..., alias="reporter_id")
    assignee_id: int | None = Field(None, alias="assignee_id")
    due_date: datetime = Field(..., alias="due_date")
    roles: models.RoleDto = Field(...)
    level: models.LevelDto = Field(...)
    durations: list[int] = Field(...)
    priority: int = Field(..., alias="priority", le=3, ge=1)
