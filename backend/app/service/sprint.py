from typing import Any
from collections import defaultdict
import logging

from app import models, utils, crud
from sqlalchemy.orm import Session
from sqlalchemy import nullslast, asc, desc


def assemble_sprint(
    db: Session, sprint_create: models.SprintCreate
) -> tuple[models.SprintDto, Any]:
    # get all tickets sprint_id is Null order by due_date(asc, None as inf), priority(desc)

    tickets = (
        db.query(models.Ticket)
        .filter(models.Ticket.sprint_id == None)
        .order_by(nullslast(asc(models.Ticket.due_date)), desc(models.Ticket.priority))
        .all()
    )

    ticket_review_dict = defaultdict(list)

    for ticket in tickets:
        if ticket.durations:
            ticket_review_dict[ticket.id] = [
                (duration.user_id, duration.duration) for duration in ticket.durations
            ]

    for ticket in tickets:
        ticket_review_dict[ticket.id].sort(key=lambda x: x[1])

    # # assemble tickets by users
    user_hours = {}
    for user in sprint_create.users:
        user_hours[user.id] = user.hours * sprint_create.duration

    user_tickets_sprint = {}

    for user in sprint_create.users:
        user_tickets_sprint[user.id] = {
            "user_data": {
                "id": user.id,
                "username": user.id,
                "hours": user_hours.get(user.id, 0),
            },
            "tickets": [],
        }

    db_sprint = models.Sprint()
    db_sprint.duration = sprint_create.duration
    db_sprint.target = sprint_create.target
    db_sprint.is_finished = False
    db.add(db_sprint)
    db.commit()
    db.refresh(db_sprint)

    for ticket in tickets:
        for user_id, duration in ticket_review_dict[ticket.id]:
            if user_hours[user_id] >= duration:
                user_hours[user_id] -= duration
                ticket.sprint_id = db_sprint.id
                ticket.assignee_id = user_id
                db.merge(ticket)
                db.commit()
                db.refresh(ticket)
                user_tickets_sprint[user_id]["tickets"].append(
                    utils.ticket.assemble_ticket_dto(ticket)
                )
                break
            else:
                logging.warning(
                    f"User {user_id} has not enough hours to complete ticket {ticket.id}"
                )

    sprint = models.SprintDto(
        id=db_sprint.id,
        duration=sprint_create.duration,
        target=sprint_create.target,
        is_finished=False,
        users=[value for key, value in user_tickets_sprint.items()],
    )

    db_sprint.duration = sprint_create.duration
    db_sprint.target = sprint_create.target

    # add mailing tasks

    return sprint, user_tickets_sprint.items()


def update(db: Session, payload: models.SprintDto) -> models.SprintDto:
    crud.sprint.update(db, payload.id, payload)
    return payload
