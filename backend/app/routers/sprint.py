from typing import Annotated, Optional

from app import models, schemas, service, utils
from app.dependencies import current_user, get_db
from fastapi import APIRouter, Body, Depends, status, BackgroundTasks
from sqlalchemy.orm import Session

router = APIRouter(prefix="/sprint", tags=["sprint"])


@router.post(
    "/",
    response_model=models.SprintDto,
    status_code=status.HTTP_201_CREATED,
)
async def create_(
    background_tasks: BackgroundTasks,
    sprint_create: models.SprintCreate = Body(...),
    db: Session = Depends(get_db),
    user: models.User = Depends(current_user),
):
    """Создание распределения задач по членам команды

    Args:
        sprint_create (models.SprintCreate, optional): данные о рабочих часах членов команды
        db (Session, optional):  сессия бд
        user (models.User, optional): авторизованный пользователь

    Returns:
        models.SprintDto
    """

    response, users = service.sprint.assemble_sprint(db, sprint_create)
    # print(users)
    return response


@router.put("/", response_model=models.SprintDto)
async def update_(
    payload: models.SprintDto = Body(...),
    db: Session = Depends(get_db),
    user: models.User = Depends(current_user),
):
    return service.sprint.update(db, payload)
