from sqlalchemy.orm import Session
from app import models


def create(db: Session, payload: models.SprintDto) -> models.Sprint:
    db_sprint = models.Sprint()

    db_sprint.duration = payload.duration
    db_sprint.target = payload.target
    db_sprint.is_finished = payload.is_finished
    db_sprint.value = payload.model_dump_json()

    db.add(db_sprint)
    db.commit()
    db.refresh(db_sprint)
    return db_sprint


def update(db: Session, _id: int, payload: models.SprintDto) -> models.Sprint:
    db_sprint = db.query(models.Sprint).filter(models.Sprint.id == _id).one_or_none()
    if not db_sprint:
        raise Exception(f"Sprint {_id} not found")

    db_sprint.value = payload.model_dump_json()
    db_sprint.is_finished = False
    db.commit()
    return db_sprint


# def get(db: Session, _id: int) -> models.SprintDto:
#     """Получение спринта по id

#     Args:
#         db (Session): сессия к бд
#         _id (int): id роли

#     Returns:
#         models.SprintDto: данные спринта
#     """
#     db_sprint = db.query(models.Sprint).filter(models.Sprint.id == _id).one_or_none()

#     # fill SprintDto
#     db_sprint_dto = models.SprintDto.model_validate(db_sprint)
#     db_sprint_dto.id = db_sprint.id
#     db_sprint_dto.duration = db_sprint.duration
#     db_sprint_dto.target = db_sprint.target
#     db_sprint_dto.is_finished = db_sprint.is_finished

#     db_sprint_dto.users = {}

#     if not db_sprint:
#         raise Exception(f"Sprint with id {_id} not found")
#     return db_sprint_dto

# def update(db: Session, payload: models.SprintDto) -> models.Sprint:
#     """Обновление рапсределения задач по стринту

#     Args:
#         db (Session): _description_
#         payload (models.SprintDto): _description_

#     Raises:
#         Exception: _description_

#     Returns:
#         models.Sprint: _description_
#     """
#     db_sprint = (
#         db.query(models.Sprint).filter(models.Sprint.id == payload.id).one_or_none()
#     )

#     if not db_sprint:
#         raise Exception(f"Sprint with id {payload.id} not found")

#     db_sprint.duration = payload.duration
#     db_sprint.target = payload.target
#     db_sprint.is_finished = payload.is_finished

#     new_ids = []
#     for user in payload.users:
#         user_data = user["user_data"]
#         tickets = user["tickets"]

#         for ticket_id in [ticket["id"] for ticket in tickets]:
#             db_ticket = (
#                 db.query(models.Ticket)
#                 .filter(models.Ticket.id == ticket_id)
#                 .one_or_none()
#             )

#             if db_ticket is None:
#                 continue

#             db_ticket.assignee_id = user_data["id"]
#             db.merge(db_ticket)
#             db.commit()
#             db.refresh(db_ticket)

#     db.commit()
#     db.refresh(db_sprint)
#     return db_sprint
