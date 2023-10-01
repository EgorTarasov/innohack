from typing import Annotated, Optional

from app import models, schemas, service, utils
from app.dependencies import current_user, get_db
from fastapi import (
    APIRouter,
    Body,
    Depends,
    FastAPI,
    File,
    HTTPException,
    Path,
    Query,
    Request,
    Response,
    UploadFile,
    status,
)
from sqlalchemy.orm import Session

router = APIRouter(prefix="/sprint", tags=["sprint"])


@router.post(
    "/",
    response_model=models.SprintDto,
    status_code=status.HTTP_201_CREATED,
)
async def create_(
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
    return service.sprint.assemble_sprint(db, sprint_create)


@router.put("/", response_model=models.SprintDto)
async def update_(
    payload: models.SprintDto = Body(...),
    db: Session = Depends(get_db),
    user: models.User = Depends(current_user),
):
    return service.sprint.update(db, payload)