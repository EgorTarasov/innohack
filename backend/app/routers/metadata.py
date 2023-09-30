from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app import crud, models

router = APIRouter(prefix="/metadata", tags=["data"])


@router.post("/role/create", response_model=models.RoleDto)
async def create_role(
    db: Session = Depends(get_db),
    payload: models.RoleCreate = Body(...),
) -> models.RoleDto:
    return models.RoleDto.model_validate(crud.role.create(db, payload))


@router.post("/level/create", response_model=models.LevelDto)
async def create_level(
    db: Session = Depends(get_db), payload: models.LevelCreate = Body(...)
):
    return models.LevelDto.model_validate(crud.level.create(db, payload))
