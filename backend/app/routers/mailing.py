from fastapi import APIRouter, Depends, HTTPException, status

from app import models, service
from app.dependencies import get_db, current_user

router = APIRouter(prefix="/mail", tags=["mail"])


@router.post(
    "/",
)
async def send_mail(
    target_mail: str,
    # user: models.User = Depends(current_user),
    db=Depends(get_db),
) -> None:
    # target_user = await service.user.get_by_email(db, email=target_mail)

    await service.mailing.send_mailing(
        to=target_mail,
        subject="Test",
        template_name="test",
        template_data={
            "ticket_name": "ticket",
            "user_name": target_mail,
            "ticket_status": "pending",
        },
    )
