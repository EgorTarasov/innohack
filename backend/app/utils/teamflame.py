import logging

import requests as requests
from app import models


def board_ids_by_user(bearer_token: str) -> list[int]:
    """Получение досок по пользователю"""
    try:
        response = requests.get(
            f"https://api.teamflame.ru/board/boardsByUser",
            headers={"Authorization": f"Bearer {bearer_token}"},
        )
        response.raise_for_status()
        return [board["id"] for board in response.json()]
    except Exception as e:
        logging.error(f"Error get boards by user: {e}")
        raise Exception(f"Error get boards by user: {e}")


def get_bearer(user: models.User):
    try:
        response = requests.post(
            f"https://api-auth.teamflame.ru/auth/signin",
            data={
                "password": user.hashed_password,
                "email": user.email
            },
        )
        response.raise_for_status()
        return response.json()["accessToken"]["token"]
    except Exception as e:
        logging.error(f"Error get tasks by user: {e}")
        raise Exception(f"Error get tasks by user: {e}")


def get_user_tasks(bearer_token: str) -> list[dict]:
    """Получение задач по пользователю"""
    try:
        response = requests.get(
            f"https://api.teamflame.ru/task/my",
            headers={"Authorization": f"Bearer {bearer_token}"},
        )
        response.raise_for_status()
        return response.json()
    except Exception as e:
        logging.error(f"Error get tasks by user: {e}")
        raise Exception(f"Error get tasks by user: {e}")


res = get_user_tasks(
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InRlc3Q5MjM4MTA4MzEyMDk4MzkwMUB0ZXN0LmNvbSIsInVzZXJJZCI6IjY1MThmNDkxODc5OTgyYzIwZjBjZWU0NyIsImlhdCI6MTY5NjEzNTk1MSwiZXhwIjoxNjk2NDM1OTUxfQ.6H1oyKjcLbYV1FHvTl92-lU1z-JJZA_MNBJLeutavJs")
pass
