"""
- "ticket/" post Создание задач
- "ticket/" get Получение всех задач

- "ticket/{ticket_id}" get Получение задачи по id
- "ticket/{ticket_id}" put Изменение задачи по id
- "ticket/{ticket_id}" delete Удаление задачи по id
- "ticket/{ticket_id}/review" post добавление duration к задаче
- "ticket/{ticket_id}/review" put изменение duration к задаче

"""

from fastapi import APIRouter, Depends, status, Response, Request, Body, HTTPException
from app import models, service

from sqlalchemy.orm import Session
from app.dependencies import get_db, current_user


router = APIRouter(prefix="", tags=["ticket"])


@router.post(
    "/ticket",
    response_model=models.TicketCreate,
    status_code=status.HTTP_201_CREATED,
)
async def create_ticket(
    ticket: models.TicketCreate = Body(...),
    db: Session = Depends(get_db),
    user: models.User = Depends(current_user),
):
    """
    Create a new ticket.
    """
    return service.ticket.create(db, ticket, user)

@router.get(
    "/ticket",
    response_model=models.TicketDto,
    status_code=status.HTTP_200_OK,
)
async def get_ticket(
    request: Request,
    response: Response,
    db: Session = Depends(get_db),
    user: models.User = Depends(current_user),
):
    """
    Get all tickets.
    """
    return service.ticket.get_all(db, user)

@router.get(
    "/ticket/{ticket_id}/review"
)
async def review(
    ticket_id: int,
    db: Session = Depends(get_db),
    user: models.User = Depends(current_user),
):
    return service.ticket.review(db, ticket_id, user)

