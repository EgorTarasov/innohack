import csv
from datetime import datetime

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


def upload_csv(db: Session, csv_reader: csv.DictReader) -> list[models.Ticket]:
    """Загрузка задач из csv

    Args:
        csv_reader (csv.DictReader): csv reader
        user (models.User): пользователь
        :param csv_reader:
        :param db:
    """

    tickets = utils.parsers.csv_reader_to_tickets(csv_reader)
    tickets = crud.ticket.bulk_create(db, tickets)
    return tickets


def get_from_teamflame(db: Session, user: models.User) -> list[models.Ticket]:
    """Получение задач по пользователю

    Args:
        user (models.User): пользователь

    Returns:
        list[dict]: список задач
        :param user:
        :param db:
    """

    bearer_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InRlc3Q5MjM4MTA4MzEyMDk4MzkwMUB0ZXN0LmNvbSIsInVzZXJJZCI6IjY1MThmNDkxODc5OTgyYzIwZjBjZWU0NyIsImlhdCI6MTY5NjEzNTk1MSwiZXhwIjoxNjk2NDM1OTUxfQ.6H1oyKjcLbYV1FHvTl92-lU1z-JJZA_MNBJLeutavJs"

    tickets = []
    for tf_task in utils.teamflame.get_user_tasks(bearer_token):
        ticket = db.query(models.Ticket.title == tf_task["name"]).one_or_none()
        if not (ticket is None):
            continue
        ticket = models.Ticket()
        ticket.title = tf_task["name"]
        ticket.description = tf_task["description"]
        ticket.reporter_id = user.id
        ticket.due_date = datetime.strptime(tf_task["endDate"], "%Y-%m-%dT%H:%M:%S.%fZ")
        if "middle" in tf_task["priority"]:
            ticket.priority = 2
        elif "high" in tf_task["priority"]:
            ticket.priority = 3
        else:
            ticket.priority = 1
        ticket.role_id = 1
        ticket.level_id = 2

        tickets.append(ticket)

    db.add_all(tickets)
    db.commit()
    for ticket in tickets:
        db.refresh(ticket)
    
    return tickets
