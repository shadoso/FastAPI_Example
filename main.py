from uuid import UUID
from typing import List
from fastapi import FastAPI
from fastapi import HTTPException
from models import Gender, Role, Courses, User, UpdateInfo

MULT_COURSE = {Role.coordinator, Role.teacher}
MAX_COURSE = 3
MIN_COURSE = 1
NOT_FOUND = 404

app = FastAPI()

database: List[User] = [
    User(id=UUID("4fe2290d-04c5-4853-a57c-881748beaaf9"),
         name="Thomas Anderson",
         gender=Gender.male,
         role=Role.admin,
         ),
    User(
        id=UUID("e7d8c3b3-48ae-4da2-ad8d-20b638307c3f"),
        name="Vanellope Von Schweetz",
        gender=Gender.female,
        role=Role.student,
        course={Courses.cs}
    ),
    User(id=UUID("49af883d-ecf4-4542-b453-effab75d012a"),
         name="Miles Gonzalo Morales",
         gender=Gender.male,
         role=Role.teacher,
         course={Courses.cs, Courses.ds, Courses.bioeng}
         )
]


@app.get("/")
async def home():
    return {"I'm home": "Hi"}


@app.get("/college/show/users")
async def show_users():
    return database


@app.post("/college/register/users")
async def register_users(user: User):
    user.name.capitalize()

    if user.role in Role.admin:
        database.append(user)
        return f"{user.role.value}: {user.name} has been added, ID: {user.id}"

    if user.role in MULT_COURSE and len(user.course) <= MAX_COURSE:
        database.append(user)
        return f"{user.role.value}: {user.name} has been added, ID: {user.id}"

    if user.role in Role.guest and user.course is None:
        database.append(user)
        return f"{user.role.value}: {user.name} has been added, ID: {user.id}"

    if user.role in Role.student and len(user.course) == MIN_COURSE:
        database.append(user)
        return f"{user.role.value}: {user.name} has been added, ID: {user.id}"

    else:
        return "Guests can't have courses, students can have only 1 course, staff members can have up ot 3 courses"


@app.put("/college/update/info/{user_id}")
async def update_users(user_id: UUID, update: UpdateInfo):
    for user in database:

        if user.id == user_id:
            backup = user.copy()
            user.role = update.role
            user.course = update.course
            return "Old", backup, "New", user

    raise HTTPException(
        status_code=404,
        detail=f"The id {user_id} doesn't belong to any user"
    )


@app.delete("/college/delete/users/{user_id}")
async def delete_users(user_id: UUID):
    for user in database:
        if user.id == user_id:
            database.remove(user)
            return f"User {user.name} has been removed"

    raise HTTPException(
        status_code=NOT_FOUND,
        detail=f"The id {user_id} doesn't belong to any user"
    )
