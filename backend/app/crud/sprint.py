from sqlalchemy.orm import Session
from app import models


def create(db: Session, payload: models.SprintDto) -> models.Sprint:
    db_sprint = models.Sprint()

    db_sprint.duration = payload.duration
    db_sprint.target = payload.target
    db_sprint.is_finished = payload.is_finished

    db.add(db_sprint)
    db.commit()
    db.refresh(db_sprint)
    return db_sprint


def get(db: Session, _id: int) -> models.SprintDto:
    """Получение спринта по id

    Args:
        db (Session): сессия к бд
        _id (int): id роли

    Returns:
        models.SprintDto: данные спринта
    """
    db_sprint = db.query(models.Sprint).filter(models.Sprint.id == _id).one_or_none()

    # fill SprintDto
    db_sprint_dto = models.SprintDto()
    db_sprint_dto.id = db_sprint.id
    db_sprint_dto.duration = db_sprint.duration
    db_sprint_dto.target = db_sprint.target
    db_sprint_dto.is_finished = db_sprint.is_finished
    
    db_sprint_dto.users = {}
    

    if not db_sprint:
        raise Exception(f"Sprint with id {_id} not found")
    return db_sprint
