from uuid import UUID
from fastapi import FastAPI
from fastapi import HTTPException
from models import User
from PostgreSQL import DataBase

NOT_FOUND = 404

app = FastAPI()


@app.get("/")
async def home():
    return {"I'm home": "Hi"}


@app.get("/college/show/users")
async def show_users():
    return 0


@app.post("/college/register/users")
async def register_users(user: User):
    user.name.capitalize()

    database = DataBase(
        user_uid=user.uid,
        name=user.name,
        gender=user.gender,
        role=user.role,
        course=user.course,
        salary=user.salary,
        monthly_payment=user.monthly_payment,
        scholarship=user.scholarship,
        disabilities=user.disabilities
    )
    database.register_user()
    database.close_db()

    return f"User: {user.name} has been created"

# @app.put("/college/update/info/{user_id}")
# async def update_users(user_id: UUID, update: UpdateInfo):
#     for user in database:
#
#         if user.id == user_id:
#             backup = user.copy()
#             user.role = update.role
#             user.course = update.course
#             return "Old", backup, "New", user
#
#     raise HTTPException(
#         status_code=404,
#         detail=f"The id {user_id} doesn't belong to any user"
#     )
#
#
# @app.delete("/college/delete/users/{user_id}")
# async def delete_users(user_id: UUID):
#     for user in database:
#         if user.id == user_id:
#             database.remove(user)
#             return f"User {user.name} has been removed"
#
#     raise HTTPException(
#         status_code=NOT_FOUND,
#         detail=f"The id {user_id} doesn't belong to any user"
#     )
