from app import models, schemas


def assemble_ticket_dtos(tickets: list[models.Ticket]):
    return [assemble_ticket_dto(ticket) for ticket in tickets]


def assemble_ticket_dto(ticket: models.Ticket) -> schemas.TicketDto:
    return schemas.TicketDto(
        id=ticket.id,
        sprint_id=ticket.sprint_id,
        title=ticket.title,
        description=ticket.description,
        reporter_id=ticket.reporter_id,
        assignee_id=ticket.assignee_id,
        due_date=ticket.due_date,
        roles=ticket.role,
        level=ticket.level,
        priority=ticket.priority,
        durations=[int(item.duration) for item in ticket.durations],
    )
