from sqlalchemy.orm import Session
from app import crud, models, schemas


def create(
    db: Session, ticket: models.TicketCreate, user: models.User
) -> schemas.TicketDto:
    #FIXME not enough fields)
    """Создание задачи

    Args:
        db (Session): сессия к бд
        ticket (models.TicketCreate): данные задачи
        user (models.User): пользователь

    Returns:
        models.TicketDto: данные задачи
    """
    db_ticket = crud.ticket.create(db, ticket)
    return schemas.TicketDto.model_validate(db_ticket)


def get_all(db: Session, user: models.User):
    """Получение всех задач

    Args:
        db (Session): сессия к бд
        user (models.User): пользователь

    Returns:
        list[models.TicketDto]: список задач
    """

    return crud.ticket.get_all(db)


def get(db: Session, ticket_id: int) -> schemas.TicketDto:
    """Получение задачи по id

    Args:
        db (Session): сессия к бд
        ticket_id (int): id задачи
        user (models.User): пользователь

    Returns:
        models.TicketDto: данные задачи
    """
    db_ticket = crud.ticket.get(db, ticket_id)
    roles = [
        models.RoleDto.model_validate(role)
        for role in crud.role.get_list(db, db_ticket.role_ids)
    ]
    level = models.LevelDto.model_validate(crud.level.get(db, db_ticket.level_id))
    return schemas.TicketDto(
        id=db_ticket.id,
        sprint_id=db_ticket.sprint_id,
        title=db_ticket.title,
        description=db_ticket.description,
        reporter_id=db_ticket.reporter_id,
        assignee_id=db_ticket.assignee_id,
        due_date=db_ticket.due_date,
        roles=roles,
        level=level,
    )


def update(db: Session, payload: models.TicketCreate) -> schemas.TicketDto:
    """Обновление задачи

    Args:
        db (Session): сессия к бд
        payload (models.TicketCreate): данные задачи
        user (models.User): пользователь

    Returns:
        models.TicketDto: данные задачи
    """
    db_ticket = crud.ticket.update(db, payload)
    #FIXME not enough fields)
    return schemas.TicketDto.model_validate(db_ticket)


def review(
    db: Session, payload: models.TicketReviewCreate, user: models.User
) -> models.TicketReviewDto | None:
    """Создание ревью задачи

    Args:
        db (Session): сессия к бд
        payload (models.TicketReviewCreate): Данные ревью
        user (models.User): пользователь, оставивший ревью

    Returns:
        models.TicketReviewtDto | None: обновленные данные ревью
    """
    db_ticket_review = crud.ticket_review.create(db, payload, user)
    return models.TicketReviewDto.model_validate(db_ticket_review)
