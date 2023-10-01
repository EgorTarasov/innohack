from fastapi import FastAPI
from fastapi.testclient import TestClient

from app import models, db, create_app
import random
import json
import datetime


app = create_app()
client = TestClient(app)
# db.BaseSqlModel.metadata.create_all(bind=db.engine)

auth_token: str | None = None


def get_random_ticket_data() -> datetime.datetime:
    now = datetime.datetime.now()

    year = now.year
    month = now.month

    # Get the number of days in the current month
    num_days = (datetime.date(year, month + 1, 1) - datetime.date(year, month, 1)).days

    # Generate a random day within the current month
    day = random.randint(1, num_days)

    # Create a datetime object with the random date
    return datetime.datetime(year, month, day)


def get_create_credentials(i: int | None = None):
    if i:

        return {
            "email": f"test{i}@test.com",
            "password": "test",
            "username": f"test{i}",
        }
    return {
        "email": "test@test.com",
        "password": "test",
        "username": "test",
    }


def get_login_credentials(i: int | None = None):
    if i:
        return {
            "email": f"test{i}@test.com",
            "password": "test",
        }
    return {
        "email": "test@test.com",
        "password": "test",
    }


# def test_user_create():
#     response = client.post(
#         "/user/",
#         json=get_create_credentials(),
#     )
#     assert response.status_code == 201
#     data = response.json()
#     global auth_token
#     auth_token = data["access_token"]
#     assert "access_token" in data
#     assert "token_type" in data

#     for i in range(1, 10):
#         response = client.post(
#             "/user/",
#             json=get_create_credentials(i),
#         )
#         assert response.status_code == 201
#         data = response.json()
#         assert "access_token" in data
#         assert "token_type" in data


# def test_user_login():
#     response = client.post(
#         "user/login",
#         json=get_login_credentials(),
#     )

#     assert response.status_code == 200
#     data = response.json()
#     assert "access_token" in data
#     assert "token_type" in data

#     # response = client.post(
#     #     "user/login",
#     #     data={
#     #         "email": "none",
#     #         "password": "none",
#     #     },
#     # )


def test_role_create():
    labels = [
        "Frontend",
        "Backend",
        "DevOps",
        "Data Science",
        "Machine Learning",
        "Design",
        "UI/UX",
    ]

    for label in labels:
        response = client.post(
            "/metadata/role/create",
            json={
                "label": label,
            },
        )
        assert response.status_code == 200
        data = response.json()
        assert data["label"] == label


def test_level_create():
    labels = [
        "Junior",
        "Mid",
        "Senior",
    ]

    for label in labels:
        response = client.post(
            "/metadata/level/create",
            json={
                "label": label,
            },
        )
        assert response.status_code == 200
        data = response.json()
        assert data["label"] == label


# # def test_create_ticket():
# def test_create_multiple_tickets():
#     # Create a list of ticket data

#     for i in range(30):
#         title = f"Task {i+1}: {random.choice(['University', 'IT'])} related task"
#         description = f"Description for task {i+1}: {random.choice(['University', 'IT'])} related task"
#         data = models.TicketCreate(
#             title=title,
#             description=description,
#             reporter_id=random.randint(1, 10),
#             assignee_id=None,
#             due_date=get_random_ticket_data(),
#             role_id=random.randint(1, 3),
#             priority=random.randint(1, 3),
#             level_id=random.randint(1, 3),
#         )
#         response = client.post(
#             "/ticket/create",
#             headers={
#                 "Authorization": f"Bearer {auth_token}",
#             },
#             json=json.loads(data.model_dump_json()),
#         )
#         assert response.status_code == 201
#         ticket_id = response.json()["id"]

#         # # Send a GET request to retrieve the created ticket
#         # response = client.get(f"/ticket/{ticket_id}")
#         # assert response.status_code == 200
#         # assert response.json() == data.dict()


# def test_create_multiple_ticket_reviews():

#     test_data = [
#         {
#             "ticket_id": 1,
#             "duration": 8,
#         },
#         {
#             "ticket_id": 2,
#             "duration": 12,
#         },
#         {
#             "ticket_id": 3,
#             "duration": 5,
#         },
#         {
#             "ticket_id": 4,
#             "duration": 20,
#         },
#         {
#             "ticket_id": 5,
#             "duration": 4,
#         },
#         {
#             "ticket_id": 6,
#             "duration": 21,
#         },
#         {
#             "ticket_id": 7,
#             "duration": 13,
#         },
#         {
#             "ticket_id": 8,
#             "duration": 12,
#         },
#         {
#             "ticket_id": 9,
#             "duration": 9,
#         },
#         {
#             "ticket_id": 10,
#             "duration": 8,
#         },
#         {
#             "ticket_id": 11,
#             "duration": 5,
#         },
#         {
#             "ticket_id": 12,
#             "duration": 4,
#         },
#         {
#             "ticket_id": 13,
#             "duration": 3,
#         },
#         {
#             "ticket_id": 14,
#             "duration": 9,
#         },
#         {
#             "ticket_id": 15,
#             "duration": 10,
#         },
#     ]

#     for data in test_data:
#         _id = data.pop("ticket_id")
#         response = client.post(
#             f"/ticket/{_id}/review/",
#             headers={
#                 "Authorization": f"Bearer {auth_token}",
#             },
#             json=data,
#         )
#         assert response.status_code == 200
#         assert response.json()["ticket_id"] == _id


# # drop all tables
# # db.BaseSqlModel.metadata.drop_all(bind=db.engine)
