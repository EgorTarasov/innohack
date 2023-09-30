from app import crud, models
from app.dependencies import get_db
from fastapi import APIRouter, Body, Depends
from sqlalchemy.orm import Session

router = APIRouter(prefix="/metadata", tags=["data"])


@router.post("/role/create", response_model=models.RoleDto)
async def create_role(
    db: Session = Depends(get_db),
    payload: models.RoleCreate = Body(...),
) -> models.RoleDto:
    return models.RoleDto.model_validate(crud.role.create(db, payload))


@router.get("/role/all", response_model=list[models.RoleDto])
async def get_all_roles(db: Session = Depends(get_db)):
    return models.RoleDto.model_validate(crud.role.get_all(db))


@router.post("/level/create", response_model=models.LevelDto)
async def create_level(
    db: Session = Depends(get_db), payload: models.LevelCreate = Body(...)
):
    return models.LevelDto.model_validate(crud.level.create(db, payload))


@router.get("/level/all", response_model=list[models.LevelDto])
async def get_all_levels(db: Session = Depends(get_db)):
    return models.LevelDto.model_validate(crud.level.get_all(db))
