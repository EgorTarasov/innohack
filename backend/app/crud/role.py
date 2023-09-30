from sqlalchemy.orm import Session
from app import models


def create(db: Session, payload: models.RoleCreate) -> models.Role:
    """Создание роли

    Args:
        db (Session): сессия к бд
        payload (models.RoleCreate): данные роли

    Returns:
        models.RoleDto: данные роли
    """
    db_role = models.Role(label=payload.label)
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role


def get(db: Session, _id: int) -> models.Role:
    """Получение роли по id

    Args:
        db (Session): сессия к бд
        _id (int): id роли

    Returns:
        models.RoleDto: данные роли
    """
    db_role = db.query(models.Role).filter(models.Role.id == _id).one_or_none()
    if not db_role:
        raise Exception(f"Role with id {_id} not found")
    return db_role


def get_list(db: Session, _ids: list[int]) -> list[models.Role]:
    """Получение списка ролей

    Args:
        db (Session): _description_
        _ids (list[int]): _description_

    Returns:
        list[models.Role]: _description_
    """
    db_roles = db.query(models.Role).filter(models.Role.id.in_(_ids)).all()
    return db_roles
