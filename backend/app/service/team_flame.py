import requests
import logging
from app import models
from . import mailing
from app import utils
import json


def sign_up(user: models.UserCreate) -> None:
    response = requests.post(
        url="https://auth-api.teamflame.ru/auth/sign-up",
        data=json.dumps(
            {
                "firstName": "Jane",
                "lastName": "Doe",
                "surName": "Jones",
                "password": user.password,
                "email": user.email,
            }
        ),
        headers={
            "accept": "application/json",
            "Content-Type": "application/json",
        },
    )

    if response.status_code != 201:
        raise Exception("User already exists")
    mailing.send_mailing(
        user.email,
        "Welcome to TeamFlame",
        "confirmation_email",
        {
            "user_name": user.username,
            "email": user.email,
            "password": user.password,
        },
    )
