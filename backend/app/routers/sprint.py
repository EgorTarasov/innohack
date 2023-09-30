from typing import Annotated, Optional

from app import models, schemas, service, utils
from app.dependencies import current_user, get_db
from fastapi import (APIRouter, Body, Depends, FastAPI, File, HTTPException,
                     Path, Query, Request, Response, UploadFile, status)
from sqlalchemy.orm import Session

router = APIRouter(prefix="/sprint", tags=["sprint"])


@router.post(
    "/",
    response_model=schemas.SprintDto,
    status_code=status.HTTP_201_CREATED,
)
async def create_ticket(
    sprint_create: models.SprintCreate = Body(...),
    db: Session = Depends(get_db),
    user: models.User = Depends(current_user),
):
    """
    Create a new sprint.
    """

    return service.sprint.assemble_sprint(db, sprint_create)
