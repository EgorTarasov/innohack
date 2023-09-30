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
from app import models, service, schemas

from sqlalchemy.orm import Session
from app.dependencies import get_db, current_user


router = APIRouter(prefix="/ticket", tags=["ticket"])


@router.post(
    "/create",
    response_model=schemas.TicketDto,
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
    "/all",
    response_model=list[schemas.TicketDto],
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
    "/{ticket_id}",
    response_model=schemas.TicketDto,
    status_code=status.HTTP_200_OK,
)
async def get_ticket_by_id(
    ticket_id: int,
    db: Session = Depends(get_db),
    user: models.User = Depends(current_user),
):
    """
    Get ticket by id.
    """
    try:
        return service.ticket.get(db, ticket_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail="Ticket not found")


@router.put(
    "/{ticket_id}",
    response_model=schemas.TicketDto,
    status_code=status.HTTP_200_OK,
)
async def update_ticket(
    ticket_id: int,
    ticket: models.TicketCreate = Body(...),
    db: Session = Depends(get_db),
    user: models.User = Depends(current_user),
):
    """
    Update ticket by id.
    """
    try:
        return service.ticket.update(db, ticket)
    except Exception as e:
        raise HTTPException(status_code=404, detail="Ticket not found")


@router.get("/{ticket_id}/review")
async def review(
    payload: models.TicketReviewCreate,
    db: Session = Depends(get_db),
    user: models.User = Depends(current_user),
):
    return service.ticket.review(db, payload, user)
