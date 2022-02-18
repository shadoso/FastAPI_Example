from uuid import UUID
from fastapi import FastAPI
from models import User
from PostgreSQL import DataBase

NOT_FOUND = 404

app = FastAPI()


@app.get("/")
async def home():
    return {"I'm home": "Hi"}


@app.get("/college/show/{user_id}")
async def show_users(user_uid: UUID):
    database = DataBase(user_uid)
    user = database.query_user()

    if user is None:
        return f"The UUID: {user_uid} doesn't belong to any user."

    else:
        return user


@app.delete("/college/delete/users/{user_id}")
async def delete_users(user_uid: UUID):
    database = DataBase(user_uid)
    verify = database.query_user()

    if verify is not None:
        database.delete_user()
        database.close_db()
        return f"User: {user_uid} has been removed"

    else:
        database.close_db()
        return f"The UUID: {user_uid} doesn't belong to any user."


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
    verify = database.query_user()

    if verify is None:
        database.register_user()
        database.close_db()
        return f"User: {user.uid} has been created"

    else:
        database.close_db()
        return f"The UUID: {user.uid} already have a owner"

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
