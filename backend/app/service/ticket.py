import csv

from app import crud, models, schemas, utils
from sqlalchemy.orm import Session


def create(
    db: Session, ticket: models.TicketCreate, user: models.User
) -> schemas.TicketDto:
    """Создание задачи

    Args:
        db (Session): сессия к бд
        ticket (models.TicketCreate): данные задачи
        user (models.User): пользователь

    Returns:
        models.TicketDto: данные задачи
    """
    return utils.ticket.assemble_ticket_dto(crud.ticket.create(db, ticket))


def get_all(db: Session, user: models.User):
    """Получение всех задач

    Args:
        db (Session): сессия к бд
        user (models.User): пользователь

    Returns:
        list[models.TicketDto]: список задач
    """

    return utils.ticket.assemble_ticket_dtos(crud.ticket.get_all(db))


def get_all_by_role(db: Session, role_id: int):
    """Получение всех задач по роли

    Args:
        db (Session): сессия к бд
        role_id (int): id роли

    Returns:
        list[models.TicketDto]: список задач
    """

    return utils.ticket.assemble_ticket_dtos(crud.ticket.get_all_by_role(db, role_id))


def get(db: Session, ticket_id: int) -> schemas.TicketDto:
    """Получение задачи по id

    Args:
        db (Session): сессия к бд
        ticket_id (int): id задачи
        user (models.User): пользователь

    Returns:
        models.TicketDto: данные задачи
    """
    return utils.ticket.assemble_ticket_dto(crud.ticket.get(db, ticket_id))


def update(db: Session, payload: models.TicketCreate) -> schemas.TicketDto:
    """Обновление задачи

    Args:
        db (Session): сессия к бд
        payload (models.TicketCreate): данные задачи
        user (models.User): пользователь

    Returns:
        models.TicketDto: данные задачи
    """
    return utils.ticket.assemble_ticket_dto(crud.ticket.update(db, payload))


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


def upload_csv(db: Session, csv_reader: csv.DictReader) -> list[schemas.TicketDto]:
    """Загрузка задач из csv

    Args:
        csv_reader (csv.DictReader): csv reader
        user (models.User): пользователь
    """

    tickets = utils.parsers.csv_reader_to_tickets(csv_reader)
    tickets = crud.ticket.bulk_create(db, tickets)
    return utils.ticket.assemble_ticket_dtos(tickets)
